import random
import time
import sys
import json
from functions import Question, pyt_ekspert, pyt_pub, pol_na_pol

poczatek = """
  __  __  _____  _       _____  ____   _   _  ______  _____   ________     __
 |  \/  ||_   _|| |     |_   _|/ __ \ | \ | ||  ____||  __ \ |___  /\ \   / /
 | \  / |  | |  | |       | | | |  | ||  \| || |__   | |__) |   / /  \ \_/ / 
 | |\/| |  | |  | |       | | | |  | || . ` ||  __|  |  _  /   / /    \   /  
 | |  | | _| |_ | |____  _| |_| |__| || |\  || |____ | | \ \  / /__    | |   
 |_|  |_||_____||______||_____|\____/ |_| \_||______||_|  \_\/_____|   |_|   
                                                                             
                                                                             
(start)  - początek gry
(zasady) - zasady gry
(exit)   - koniec gry
"""
ekspert = True
publicznosc = True
polnapol = True
with open("questions.json", "r") as f:
    data = json.load(f)
lvl1_questions = data["lvl1"]
lvl2_questions = data["lvl2"]
lvl3_questions = data["lvl3"]
lvl4_questions = data["lvl4"]
lvl5_questions = data["lvl5"]
lvl6_questions = data["lvl6"]
lvl7_questions = data["lvl7"]
lvl8_questions = data["lvl8"]
lvl9_questions = data["lvl9"]
lvl10_questions = data["lvl10"]


def main(pytanie):
    global ekspert
    global publicznosc
    global polnapol

    while True:
        answer = input()
        if answer == pytanie.correctAnswer:
            print("Poprawna odpowiedź!")
            return True
        elif answer != pytanie.correctAnswer and answer != "pomoc":
            print("Błędna odpowiedź!")
            return False
        elif answer == "pomoc":
            print("Wybierz którego koła chcesz uzyć:\n1. Pytanie do eksperta\n2. Pytanie do publiczności\n3. Pół na pół")
            kolo = input()
            if kolo == "1" and ekspert == True:
                pyt_ekspert(pytanie)
                ekspert = False
                print("Jaka jest twoja odpowiedź?")
            elif kolo == "1" and ekspert == False:
                print(
                    "Wykorzystałeś juz pytanie do eksperta. Podaj odpowiedź lub wpisz (pomoc) aby uzyć innego koła")
            if kolo == "2" and publicznosc == True:
                pyt_pub(pytanie)
                publicznosc = False
                print("Jaka jest twoja odpowiedź?")
            elif kolo == "2" and publicznosc == False:
                print(
                    "Wykorzystałeś juz pytanie do publiczności. Podaj odpowiedź lub wpisz (pomoc) aby uzyć innego koła")
            if kolo == "3" and polnapol == True:
                pol_na_pol(pytanie)
                polnapol = False
                print("Jaka jest twoja odpowiedź?")
            elif kolo == "3" and polnapol == False:
                print(
                    "Wykorzystałeś juz pół na pół. Podaj odpowiedź lub wpisz (pomoc) aby uzyć innego koła")

# TODO:
# ? moze user_input == "start" da się zamknąć w pętli for, zeby skrócić trochę kod


while True:
    print(poczatek)
    user_input = input()
    if user_input != "start" and user_input != "zasady" and user_input != "exit" and user_input != "pass":
        print(f"Komenda {user_input} nie istnieje. Spróbuj ponownie\n")
        time.sleep(2)

    if user_input == "start":
        while True:
            pytanie = random.choice(lvl1_questions)
            pytanie = Question(pytanie["prompt"], pytanie["answer1"], pytanie["answer2"],
                               pytanie["answer3"], pytanie["answer4"], pytanie["correctAnswer"])
            print(
                f"\nPytanie 1 - 500pln  Wpisz (pomoc), aby skorzystać z koła ratunkowego\n\n{pytanie.prompt}\n{pytanie.answer1}\n{pytanie.answer2}\n{pytanie.answer3}\n{pytanie.answer4}\n")

            if main(pytanie) == False:
                print("Niestety to koniec gry\nNie udało ci się nic wygrać :/")
                sys.exit()

            pytanie = random.choice(lvl2_questions)
            pytanie = Question(pytanie["prompt"], pytanie["answer1"], pytanie["answer2"],
                               pytanie["answer3"], pytanie["answer4"], pytanie["correctAnswer"])
            print(
                f"\nPytanie 2 - 1 000pln  Wpisz (pomoc), aby skorzystać z koła ratunkowego\n\n{pytanie.prompt}\n{pytanie.answer1}\n{pytanie.answer2}\n{pytanie.answer3}\n{pytanie.answer4}\n")

            if main(pytanie) == False:
                print("Niestety to koniec gry\nNie udało ci się nic wygrać :/")
                sys.exit()

            pytanie = random.choice(lvl3_questions)
            pytanie = Question(pytanie["prompt"], pytanie["answer1"], pytanie["answer2"],
                               pytanie["answer3"], pytanie["answer4"], pytanie["correctAnswer"])
            print(
                f"\nPytanie 3 - 5 000pln  Wpisz (pomoc), aby skorzystać z koła ratunkowego\n\n{pytanie.prompt}\n{pytanie.answer1}\n{pytanie.answer2}\n{pytanie.answer3}\n{pytanie.answer4}\n")

            if main(pytanie) == False:
                print("Niestety to koniec gry\nWygrałeś 1 000pln!")
                sys.exit()

            pytanie = random.choice(lvl4_questions)
            pytanie = Question(pytanie["prompt"], pytanie["answer1"], pytanie["answer2"],
                               pytanie["answer3"], pytanie["answer4"], pytanie["correctAnswer"])
            print(
                f"\nPytanie 4 - 10 000pln  Wpisz (pomoc), aby skorzystać z koła ratunkowego\n\n{pytanie.prompt}\n{pytanie.answer1}\n{pytanie.answer2}\n{pytanie.answer3}\n{pytanie.answer4}\n")

            if main(pytanie) == False:
                print("Niestety to koniec gry\nWygrałeś 1 000pln!")
                sys.exit()

            pytanie = random.choice(lvl5_questions)
            pytanie = Question(pytanie["prompt"], pytanie["answer1"], pytanie["answer2"],
                               pytanie["answer3"], pytanie["answer4"], pytanie["correctAnswer"])
            print(
                f"\nPytanie 5 - 20 000pln  Wpisz (pomoc), aby skorzystać z koła ratunkowego\n\n{pytanie.prompt}\n{pytanie.answer1}\n{pytanie.answer2}\n{pytanie.answer3}\n{pytanie.answer4}\n")

            if main(pytanie) == False:
                print("Niestety to koniec gry\nWygrałeś 1 000pln!")
                sys.exit()

            pytanie = random.choice(lvl6_questions)
            pytanie = Question(pytanie["prompt"], pytanie["answer1"], pytanie["answer2"],
                               pytanie["answer3"], pytanie["answer4"], pytanie["correctAnswer"])
            print(
                f"\nPytanie 6 - 40 000pln Wpisz(pomoc), aby skorzystać z koła ratunkowego\n\n{pytanie.prompt}\n{pytanie.answer1}\n{pytanie.answer2}\n{pytanie.answer3}\n{pytanie.answer4}\n")

            if main(pytanie) == False:
                print("Niestety to koniec gry\nWygrałeś 1 000pln!")
                sys.exit()

            pytanie = random.choice(lvl7_questions)
            pytanie = Question(pytanie["prompt"], pytanie["answer1"], pytanie["answer2"],
                               pytanie["answer3"], pytanie["answer4"], pytanie["correctAnswer"])
            print(
                f"\nPytanie 7 - 100 000pln Wpisz(pomoc), aby skorzystać z koła ratunkowego\n\n{pytanie.prompt}\n{pytanie.answer1}\n{pytanie.answer2}\n{pytanie.answer3}\n{pytanie.answer4}\n")

            if main(pytanie) == False:
                print("Niestety to koniec gry\nWygrałeś 40 000pln!")
                sys.exit()

            pytanie = random.choice(lvl8_questions)
            pytanie = Question(pytanie["prompt"], pytanie["answer1"], pytanie["answer2"],
                               pytanie["answer3"], pytanie["answer4"], pytanie["correctAnswer"])
            print(
                f"\nPytanie 8 - 250 000pln Wpisz(pomoc), aby skorzystać z koła ratunkowego\n\n{pytanie.prompt}\n{pytanie.answer1}\n{pytanie.answer2}\n{pytanie.answer3}\n{pytanie.answer4}\n")

            if main(pytanie) == False:
                print("Niestety to koniec gry\nWygrałeś 40 000pln!")
                sys.exit()

            pytanie = random.choice(lvl9_questions)
            pytanie = Question(pytanie["prompt"], pytanie["answer1"], pytanie["answer2"],
                               pytanie["answer3"], pytanie["answer4"], pytanie["correctAnswer"])
            print(
                f"\nPytanie 9 - 500 000pln Wpisz(pomoc), aby skorzystać z koła ratunkowego\n\n{pytanie.prompt}\n{pytanie.answer1}\n{pytanie.answer2}\n{pytanie.answer3}\n{pytanie.answer4}\n")

            if main(pytanie) == False:
                print("Niestety to koniec gry\nWygrałeś 40 000pln!")
                sys.exit()

            pytanie = random.choice(lvl10_questions)
            pytanie = Question(pytanie["prompt"], pytanie["answer1"], pytanie["answer2"],
                               pytanie["answer3"], pytanie["answer4"], pytanie["correctAnswer"])
            print(
                f"\nPytanie 10  - 1 000 000pln Wpisz(pomoc), aby skorzystać z koła ratunkowego\n\n{pytanie.prompt}\n{pytanie.answer1}\n{pytanie.answer2}\n{pytanie.answer3}\n{pytanie.answer4}\n")

            if main(pytanie) == False:
                print("Niestety to koniec gry\nWygrałeś 40 000pln!")
                sys.exit()
            else:
                print("WYGRYWASZ MILION ZŁOTYCH!\nszkoda, że tylko na niby ;(")
                sys.exit()

    elif user_input == "zasady":
        with open("/Users/shaggy/coding/python/projects/milionerzy/zasady.txt", "r") as f:
            print(f.read())
            time.sleep(10)
    elif user_input == "exit":
        sys.exit()