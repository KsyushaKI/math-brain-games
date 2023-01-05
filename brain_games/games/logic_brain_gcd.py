import random
import math


def start_game():
    return print('Find the greatest common divisor of given numbers.')


def get_question_and_correct_answer():

    first_number = random.choice(range(30))
    second_number = random.choice(range(30))
    question = f'{first_number} {second_number}'
    correct_answer = str(math.gcd(first_number, second_number))

    return question, correct_answer
