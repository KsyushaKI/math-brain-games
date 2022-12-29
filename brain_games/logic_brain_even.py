import prompt
import random


def welcome_user():
    print("Welcome to the Brain Games!")


def greeting_user():
    global name
    name = prompt.string('May I have your name? ')
    return name


def start_game():
    start_game = 'Answer "yes" if the number is even, otherwise answer "no".'
    return print(start_game)


def brain_even():
    count_of_game_rount = 3

    for _ in range(count_of_game_rount):
        random_number = random.randint(0, 100)
        question = f'Question: {random_number}'
        print(question)
        answer = prompt.string('Your answer: ')
        number_is_even = random_number % 2 == 0 and 'yes' or 'no'
        correct_result = 'Correct!'
        win_game = f'Congratulations, {name}!'
        lose_game = f"""'{answer}' is wrong answer ;(. \
            Correct answer was '{number_is_even}'.
        Let's try again, {name}!"""

        if answer != number_is_even:
            return print(lose_game)

        else:
            print(correct_result)

    return print(win_game)
