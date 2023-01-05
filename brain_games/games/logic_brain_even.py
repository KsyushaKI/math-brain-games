import random


def start_game():
    return print('Answer "yes" if the number is even, otherwise answer "no".')


def get_question_and_correct_answer():

    question = random.randint(0, 100)
    correct_answer = question % 2 == 0 and 'yes' or 'no'

    return question, correct_answer
