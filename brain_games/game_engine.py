import prompt


def greeting_user():
    print("Welcome to the Brain Games!")
    global name
    name = prompt.string('May I have your name? ')
    return name


def logic_of_brain_games(game):
    greeting_user()
    game.start_game()
    win_game = f'Congratulations, {name}!'
    correct_result = 'Correct!'
    count_of_game_round = 3

    for _ in range(count_of_game_round):
        logic_of_the_questions = game.get_question()
        print(f'Question: {logic_of_the_questions}')
        answer = prompt.string('Your answer: ')
        correct_answer = game.get_correct_answer(logic_of_the_questions)
        lose_game = (f'"{answer}" is wrong answer ;(. '
                     f'Correct answer was "{correct_answer}".'
                     f"\nLet's try again, {name}!")

        if answer != correct_answer:
            return print(lose_game)
        else:
            print(correct_result)

    return print(win_game)
