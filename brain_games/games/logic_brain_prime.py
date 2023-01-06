import random


def start_game():
    start_game = 'Answer "yes" if given number is prime. Otherwise answer "no".'

    return print(start_game)


def get_question_and_correct_answer():
    question = random.randint(2, 100)
    i = 2
    while question % i != 0:
        i += 1

    correct_answer = i == question and 'yes' or 'no'

    return question, correct_answer
