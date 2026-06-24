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
            print(i + 1, "-", workout["date"], "-", workout["exercise"])
