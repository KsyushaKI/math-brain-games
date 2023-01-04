import random


def start_game():
    return print('Answer "yes" if the number is even, otherwise answer "no".')


def get_question():
    return random.randint(0, 100)


def get_correct_answer(logic_of_the_questions):
    return logic_of_the_questions % 2 == 0 and 'yes' or 'no'
