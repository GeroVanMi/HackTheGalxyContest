import enchant
from itertools import permutations


def get_all_words(source_word: str, target_word: str):
    combinations = []
    for letter in source_word:
        combinations.append(target_word + letter)
    return combinations


def flip_characters(letters, index1, index2):
    temp = letters[index1]
    letters[index1] = letters[index2]
    letters[index2] = temp
    return letters


def compute_letter_combinations(word: str):
    """

    :param word:
    :return: array
    """
    return [''.join(index) for index in permutations(word)]


if __name__ == '__main__':
    all_combinations = []
    # Change these words here
    word_1 = 'MOROSE'
    word_2 = 'ORCA'

    all_words = get_all_words(word_1, word_2)
    d = enchant.Dict("en_US")

    for word in all_words:
        all_combinations += compute_letter_combinations(word)

    combination_set = set(all_combinations)
    for combination in combination_set:
        is_word = d.check(combination)
        if is_word:
            print(f'- {combination}')

    print('\n--------------------\n')
    # This has to be updated manually, only used to doublecheck the solution.
    # Simply remove the letter that was used to generate the solution out of word_2 and type the remaining letters
    # below.
    solution_double_check_word = 'MOROE'
    solution_set = compute_letter_combinations(solution_double_check_word)
    for combination in solution_set:
        is_word = d.check(combination)
        if is_word:
            print(f'- {combination}')