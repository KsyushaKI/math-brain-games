import random
import math


def start_game():
    return print('Find the greatest common divisor of given numbers.')


def get_question():
    first_number = random.choice(range(30))
    second_number = random.choice(range(30))
    question = f'{first_number} {second_number}'
    return question


def get_correct_answer(logic_of_the_questions):
    [a, b] = list(map(int, logic_of_the_questions.split()))
    correct_answer = math.gcd(a, b)
    return str(correct_answer)
