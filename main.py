import json
import os

USERS_FILE = "users.json"
FILE_NAME = ""

def load_users():
    try:
        with open(USERS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except:
        return {}


def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as file:
        json.dump(users, file, ensure_ascii=False, indent=4)


def register():
    users = load_users()

    print("\n=== РЕГИСТРАЦИЯ ===")

    login = input("Логин: ")

    if login in users:
        print("Такой пользователь уже существует!")
        return None

    password = input("Пароль: ")

    users[login] = password

    save_users(users)

    print("Регистрация прошла успешно!")

    return login


def login():
    users = load_users()

    print("\n=== ВХОД ===")

    login = input("Логин: ")
    password = input("Пароль: ")

    if login in users and users[login] == password:
        print("Добро пожаловать,", login)
        return login

    print("Неверный логин или пароль!")

    return None

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


def add_workout(data):
    date = input("Дата тренировки: ")
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

            print(
                i + 1,
                "-",
                workout["date"],
                "-",
                workout["exercise"]
            )


def delete_workout(data):
    if len(data["workouts"]) == 0:
        print("Удалять нечего.")
        return

    show_workouts(data)

    try:
        number = int(input("Введите номер тренировки для удаления: "))

        if 1 <= number <= len(data["workouts"]):
            deleted = data["workouts"].pop(number - 1)
            save_data(data)
            print("Тренировка удалена:",
                  deleted["date"], "-", deleted["exercise"])
        else:
            print("Такого номера нет.")

    except:
        print("Ошибка ввода!")


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

user = None

while user is None:
    print("\n1 - Войти")
    print("2 - Зарегистрироваться")
    print("0 - Выход")

    choice = input("Выберите пункт: ")

    if choice == "1":
        user = login()

    elif choice == "2":
        user = register()

    elif choice == "0":
        exit()

FILE_NAME = user + "_data.json"

data = load_data()

while True:
    print("\n=== ГЛАВНОЕ МЕНЮ ===")
    print("Пользователь:", user)
    print("1 - Добавить тренировку")
    print("2 - Показать тренировки")
    print("3 - Добавить вес")
    print("4 - История веса")
    print("5 - Установить цель")
    print("6 - Показать цель")
    print("7 - Статистика")
    print("8 - Удалить тренировку")
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
        
    elif choice == "8":
        delete_workout(data)

    elif choice == "0":
        print("\nВсе данные сохранены.")
        print("До свидания,", user)
        break

    else:
        print("Такого пункта нет.")