import json
from colorama import Fore, init
import os

init()

Welcome_Text = '''Welcome to the quiz!
You will be asked a series of questions.
Good luck!'''

def quiz(question, answer):
    print(Fore.RED + question)
    guess = input('Answer: ')
    if guess == answer:
        print('Correct!')
        add_points()
    else:
        print('Incorrect!')

def make_points():
    with open('points.json', 'w') as f:
        json.dump(0, f)

def clear_points():
    p = open('points.json', 'w')
    p.write(json.dumps(0))
    p.close()

def add_points():
    with open('points.json', 'r') as f:
        points = json.load(f)
    points += 1
    with open('points.json', 'w') as f:
        json.dump(points, f)

def show_points():
    with open('points.json', 'r') as f:
        points = json.load(f)
    if points == 0:
        print('You got no questions right')
    else:
        print(f'You got {points} questions right')

def quiz_over():
    clear_console()
    show_points()
    print(Fore.RED + 'Game Over')
    print("1. Replay the game")
    print("2. Cancel")
    again = input('What do you want to do? ')
    if again == '1':
        clear_console()
        clear_points()
        make_points()
        start_quiz()
    elif again == '2':
        clear_console()
        print(Fore.GREEN + 'Thanks for playing!')
        exit()
    else:
        clear_console()
        print('Please enter a valid response')
        quiz_over()

def clear_console():
     os.system('cls')

def start_quiz():
    print("1. Play the game")
    print("2. Cancel")
    start = input("What do you want to do? ")
    if start == '1':
      print(Fore.GREEN + Welcome_Text)
      quiz('What is the capital of the United States?', 'Washington D.C.')
      quiz('What is the capital of Canada?', 'Ottawa')
      quiz('What is the capital of France?', 'Paris')
      quiz('What is the capital of Germany?', 'Berlin')
      quiz('What is the capital of Italy?', 'Rome')
      quiz('What is the capital of the United Kingdom?', 'London')
      quiz_over()
      clear_console()
      clear_points()
    elif start == '2':
        clear_console()
        print(Fore.GREEN + 'Thanks for playing!')
        exit()
    else:
        clear_console()
        print('Please enter a valid response')
        start_quiz()

make_points()
start_quiz()