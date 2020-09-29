"""
Script to find all strings of length n that can be found from the alphabet

Author: Dominique Massau
Date: 28/09/2020
"""

# imports
from sys import argv


# functions
def parse_symbols_int(text_file: str) -> tuple:
    """
    Parse 1 - 10 symbols and an integer indicating the length of combinations

    Text file must contain 1 - 10 symbols (separated by spaced) on the first
    line and an integer on the second line. The integer indicates the length
    of the combinations that are made with the symbols. For example, a length
    of 2 with symbols A and T will lead to AA, AT, TA and TT.

    :param text_file: str, name of the text file with symbols and an integer
    :return: tuple, a list with symbols and an integer
    """

    with open(text_file, 'r') as lines:
        for line in lines:
            if len(line.strip()) > 1:
                symbols = line.strip().split(' ')
            elif line.strip().isdigit():
                integer = int(line.strip())

    return symbols, integer


def find_combinations(integer: int, symbol_list: list) -> list:
    """
    Find all permutations of length x (integer)

    Based on a given integer, identify all possible combinations that can be
    made based with the symbols, given a certain length.

    :param integer: int, maximum length of each combination
    :param symbol_list: list, all symbols to be considered
    :return: list, all permutations that are possible
    """

    length = 1

    permutations = [[number] for number in range(1, len(symbol_list) + 1)]
    while length < integer:
        temp_list = []
        for perm in permutations:
            for i in range(1, len(symbols) + 1):
                temp_list.append(perm + [i])
        permutations = temp_list
        length += 1

    return permutations


def integers_to_symbols(permutations: list, symbol_list: list) -> list:
    """
    Translate the combinatory numbers to given symbols

    :param permutations: list, sub lists with numerical combinations
    :param symbol_list: list, symbols to be combined
    :return: list, symbolic combinations
    """

    symb_combos = []
    for sublist in permutations:
        symb_combos.append([symbol_list[integer - 1] for integer in sublist])
    return sorted(symb_combos)


def report_combinations(combinational_list: list):
    """
    Write all combinations from a given symbol list to a file

    :param combinational_list: list, symbolic combinations
    """

    with open("answer_file", 'w') as writer:
        for combo in combinational_list:
            print(combo)
            writer.write(f"{''.join(combo)}\n")


if __name__ == "__main__":
    symbols, length_int = parse_symbols_int(argv[1])
    combinations = find_combinations(length_int, symbols)
    symbolic_combinations = integers_to_symbols(combinations, symbols)
    report_combinations(symbolic_combinations)
