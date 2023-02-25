import json

while True:
    pula = input("do której puli jest pytanie: ")
    prompt = input("treść pytania: ")
    answer1 = input("odpowiedź a: ")
    answer2 = input("odpowiedź b: ")
    answer3 = input("odpowiedź c: ")
    answer4 = input("odpowiedź d: ")
    correctAnswer = input("poprawna odpowiedź: ")

    json_file = {
        "prompt": prompt,
        "answer1": answer1,
        "answer2": answer2,
        "answer3": answer3,
        "answer4": answer4,
        "correctAnswer": correctAnswer
    }

    with open("/Users/shaggy/coding/python/projects/milionerzy/questions.json", "r+") as f:
        file_data = json.load(f)
        file_data[pula].append(json_file)
        f.seek(0)
        json.dump(file_data, f, indent=4)