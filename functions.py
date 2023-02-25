import random
import time
import json


class Question:
    def __init__(self, prompt, answer1, answer2, answer3, answer4, correctAnswer):
        self.prompt = prompt
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4
        self.correctAnswer = correctAnswer


def pyt_ekspert(pytanie):
    print("Zatem łączymy się z ekspertem!")
    for i in range(1, 4):
        print(".." * i)
        time.sleep(1)
    print(
        f"Zdaniem eksperta poprawna odpowiedź to odpowiedź {pytanie.correctAnswer}")


def pyt_pub(pytanie):
    print("Zatem spytajmy się publiczności")
    for i in range(1, 4):
        print(".." * i)
        time.sleep(1)
    if pytanie.correctAnswer == "A":
        pula = 100
        a = random.randint(50, 75)
        pula -= a
        b = random.randint(1, pula)
        pula -= b
        c = random.randint(1, pula)
        pula -= c
        d = pula
        print(
            f"Odpowiedzi publiczności:\nA. {a}%\nB. {b}%\nC. {c}%\nD. {d}%\n\n")
    if pytanie.correctAnswer == "B":
        pula = 100
        b = random.randint(50, 75)
        pula -= b
        a = random.randint(1, pula)
        pula -= a
        c = random.randint(1, pula)
        pula -= c
        d = pula
        print(
            f"Odpowiedzi publiczności:\nA. {a}%\nB. {b}%\nC. {c}%\nD. {d}%\n\n")
    if pytanie.correctAnswer == "C":
        pula = 100
        c = random.randint(50, 75)
        pula -= c
        a = random.randint(1, pula)
        pula -= a
        b = random.randint(1, pula)
        pula -= b
        d = pula
        print(
            f"Odpowiedzi publiczności:\nA. {a}%\nB. {b}%\nC. {c}%\nD. {d}%\n\n")
    if pytanie.correctAnswer == "D":
        pula = 100
        d = random.randint(50, 75)
        pula -= d
        a = random.randint(1, pula)
        pula -= a
        b = random.randint(1, pula)
        pula -= b
        c = pula
        print(
            f"Odpowiedzi publiczności:\nA. {a}%\nB. {b}%\nC. {c}%\nD. {d}%\n\n")


def pol_na_pol(pytanie):
    print("Zatem odrzucamy dwie błędne odpowiedzi")
    for i in range(1, 4):
        print(".." * i)
        time.sleep(1)
    if pytanie.correctAnswer == "A":
        if random.randint(1, 2) == 1:
            print(random.choice(
                [pytanie.answer2, pytanie.answer3, pytanie.answer4]))
            print(pytanie.answer1)
        else:
            print(pytanie.answer1)
            print(random.choice(
                [pytanie.answer2, pytanie.answer3, pytanie.answer4]))
    elif pytanie.correctAnswer == "B":
        if random.randint(1, 2) == 1:
            print(random.choice(
                [pytanie.answer1, pytanie.answer3, pytanie.answer4]))
            print(pytanie.answer2)
        else:
            print(pytanie.answer2)
            print(random.choice(
                [pytanie.answer1, pytanie.answer3, pytanie.answer4]))
    elif pytanie.correctAnswer == "C":
        if random.randint(1, 2) == 1:
            print(random.choice(
                [pytanie.answer2, pytanie.answer1, pytanie.answer4]))
            print(pytanie.answer3)
        else:
            print(pytanie.answer3)
            print(random.choice(
                [pytanie.answer2, pytanie.answer1, pytanie.answer4]))
    elif pytanie.correctAnswer == "D":
        if random.randint(1, 2) == 1:
            print(random.choice(
                [pytanie.answer2, pytanie.answer3, pytanie.answer1]))
            print(pytanie.answer4)
        else:
            print(pytanie.answer4)
            print(random.choice(
                [pytanie.answer2, pytanie.answer3, pytanie.answer1]))