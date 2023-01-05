import random


def start_game():
    return print('What is the result of the expression?')


def get_question_and_correct_answer():

    first_operand = random.choice(range(10, 20))
    operator = random.choice(['+', '-', '*'])
    second_operand = random.choice(range(10))

    question = f'{first_operand} {operator} {second_operand}'
    correct_answer = str(eval(question))

    return question, correct_answer
