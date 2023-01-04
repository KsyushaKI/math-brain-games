import random


def start_game():
    return print('What is the result of the expression?')


def get_question():
    first_operand = random.choice(range(10, 20))
    operator = random.choice(['+', '-', '*'])
    second_operand = random.choice(range(10))
    question = f'{first_operand} {operator} {second_operand}'
    return question


def get_correct_answer(logic_of_the_questions):
    return str(eval(logic_of_the_questions))
