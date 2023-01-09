import prompt


def greeting_user():

    print("Welcome to the Brain Games!")
    global name
    name = prompt.string('May I have your name? ')

    return print(f'Hello, {name}!')


def logic_of_brain_games(game):

    greeting_user()
    game.start_game()
    win_game = f'Congratulations, {name}!'
    correct_result = 'Correct!'
    count_of_game_round = 3

    for _ in range(count_of_game_round):
        question, correct_answer = game.get_question_and_correct_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        lose_game = (f'"{user_answer}" is wrong answer ;(. '
                     f'Correct answer was "{correct_answer}".'
                     f"\nLet's try again, {name}!")

        if user_answer != correct_answer:
            return print(lose_game)
        else:
            print(correct_result)

    return print(win_game)
