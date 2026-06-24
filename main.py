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
        json.dump(data, file, ensure_ascii=False, indent=4)def add_workout(data):
    data = input("Дата тренировки: ")
    exercise = input("Упражнение: ")

    workout = {
        "date": date,
        "exercise": exercise
    }

    data["workouts"].append(workout)
    save_data(data)

    print("Тренировка добавлена!")

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

