"""
Script to find a substring in a string

Author: Dominique Massau
Date: 25/09/2020
"""

# imports
from nucleotide_count import is_valid_sequence
from sys import argv


# functions
def parse_strings(text_file: str) -> tuple:
    """
    Parse a string and a substring from a text file

    :param text_file: str, name of the text file
    :return: tuple, contains a string and a substring
    """

    with open(text_file, 'r') as lines:
        string_list = lines.readlines()
    string = string_list[0].strip().lower()
    substring = string_list[1].strip().lower()
    return string, substring


def substring_compare_string(string: str, substring: str):
    """
    Determine positions where the substring is contained in the string

    :param string: str, a string
    :param substring: str, a substring
    :return: list, contains the start position of the substring in the string
    """

    start_pos_substring = []
    for i in range(len(string)):
        if string[i:i + len(substring)] == substring:
            start_pos_substring.append(str(i + 1))
    return start_pos_substring


if __name__ == "__main__":
    dna_string, dna_substring = parse_strings(argv[1])
    if is_valid_sequence(dna_string) and is_valid_sequence(dna_substring):
        start_pos_list = substring_compare_string(dna_string, dna_substring)
        print(' '.join(start_pos_list))