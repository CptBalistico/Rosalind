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
                integer = line.strip()

    return symbols, integer


if __name__ == "__main__":
    print(parse_symbols_int(argv[1]))
