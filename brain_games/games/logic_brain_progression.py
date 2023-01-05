import random


def start_game():
    return print('What number is missing in the progression?')


def get_question_and_correct_answer():

    list_of_progression = []
    first_number = random.randint(0, 20)
    step_of_progression = random.randint(1, 10)
    length_of_progression = random.randint(5, 10)

    for _ in range(length_of_progression):
        first_number += step_of_progression
        list_of_progression.append(first_number)

    random_index = random.randint(0, length_of_progression - 1)
    missed_element = str(list_of_progression[random_index])

    list_of_progression[random_index] = '..'
    list_of_progression = " ".join(map(str, list_of_progression))

    return list_of_progression, missed_element
