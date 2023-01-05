import random


def start_game():
    return print('Answer "yes" if given number is prime. Otherwise answer "no".')


def get_question_and_correct_answer():
    question = random.randint(0, 100)
    i = 2
    number_of_divisors = 0

    while i <= question:
        if question % i == 0:
            number_of_divisors += 1
        i += 1
        if number_of_divisors > 1:
            break

    if question <= 1 or number_of_divisors > 1:
        correct_answer = 'no'
    else:
        correct_answer = 'yes'

    return question, correct_answer
