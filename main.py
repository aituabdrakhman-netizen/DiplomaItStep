import json

FILE_NAME = "data.json"


def load_data():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except:
        return {
            "workouts": [],
            "weights": [],
            "goal": ""
        }
    
def save_data(data):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
        return
    
    data = input("Дата тренировки: ")
    exercise = input("Упражнение: ")

    workout = {
        "date": date,
        "exercise": exercise
    }

    data["workouts"].append(workout)
    save_data(data)

    print("Тренировка добавлена!")
    
def add_workout(data):
    date = input("Дата тренировки: ")
    exercise = input("Упражнение: ")

    workout = {
        "date": date,
        "exercise": exercise
    }

def show_workouts(data):
    if len(data["workouts"]) == 0:
        print("Тренировок нет.")
    else:
        print("\n=== ТРЕНИРОВКИ ===")
        for i in range(len(data["workouts"])):
            workout = data["workouts"][i]
            print(i + 1, "-", workout["date"], "-", workout["exercise"])

def add_weight(data):
    try:
        weight = float(input("Введите вес: "))
        data["weights"].append(weight)
        save_data(data)
        print("Вес сохранён.")
    except:
        print("Ошибка ввода!")


def show_weights(data):
    if len(data["weights"]) == 0:
        print("История веса пуста.")
    else:
        print("\n=== ИСТОРИЯ ВЕСА ===")
        for weight in data["weights"]:
            print(weight, "кг")


def set_goal(data):
    goal = input("Введите цель: ")
    data["goal"] = goal
    save_data(data)
    print("Цель сохранена.")


def show_goal(data):
    if data["goal"] == "":
        print("Цель не установлена.")
    else:
        print("Текущая цель:", data["goal"])

def show_statistics(data):
    print("\n=== СТАТИСТИКА ===")
    print("Количество тренировок:", len(data["workouts"]))

    if len(data["weights"]) > 0:
        print("Последний вес:", data["weights"][-1], "кг")
    else:
        print("Вес ещё не добавлялся.")

    if data["goal"] != "":
        print("Текущая цель:", data["goal"])
    else:
        print("Цель не установлена.")

print("=" * 35)
print("      ДОБРО ПОЖАЛОВАТЬ")
print("         В FITTRACKER")
print("=" * 35)
print("Персональный фитнес-дневник")
print()

data = load_data()

while True:
    print("\n=== ГЛАВНОЕ МЕНЮ ===")
    print("1 - Добавить тренировку")
    print("2 - Показать тренировки")
    print("3 - Добавить вес")
    print("4 - История веса")
    print("5 - Установить цель")
    print("6 - Показать цель")
    print("7 - Статистика")
    print("0 - Выход")

    choice = input("Выберите пункт: ")

    if choice == "1":
        add_workout(data)

    elif choice == "2":
        show_workouts(data)

    elif choice == "3":
        add_weight(data)

    elif choice == "4":
        show_weights(data)

    elif choice == "5":
        set_goal(data)

    elif choice == "6":
        show_goal(data)

    elif choice == "7":
        show_statistics(data)

    elif choice == "0":
        print("\nВсе данные сохранены.")
        print("Спасибо за использование FitTracker!")
        print("До свидания!")
        break

    else:
        print("Такого пункта нет.")