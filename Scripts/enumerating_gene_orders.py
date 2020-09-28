"""
Script to report the number of permutations and all of those

Author: Dominique Massau
Date: 28/09/2020
"""

# imports
from sys import argv


# functions
def parse_int(text_file: str) -> int:
    """
    Parse a single integer from a text file

    :param text_file: str, name of file with an integer
    :return: int, integer
    """

    with open(text_file, 'r') as lines:
        for line in lines:
            return int(line.strip())


def find_combinations(integer: int) -> list:
    """
    Find all permutations of length x (integer)

    Based on a given integer, identify all possible combinations that can be
    made based on the numbers between 1 and the integer. Calling the function
    with 3 as integer, this results in a total of six different combinations:
    3 * 2 * 1 = 6. Each combination of numbers is reported as list of lists

    :param integer: int, maximum length of each combination
    :return: list, all permutations that are possible
    """

    length = 1

    # create a separate list for each unique element
    permutations = [[number] for number in range(1, integer + 1)]
    while length < integer:
        temp_list = []
        for perm in permutations:
            for i in range(1, integer + 1):
                if i not in perm:
                    temp_list.append(perm + [i])
        permutations = temp_list
        length += 1

    return permutations


def report_combinations(permutations: list):
    """
    Report different combinations of integers and write output to a file

    :param permutations: list, contains all permutations that are possible
    """

    with open("answer_file", 'w') as writer:
        writer.write(f"{len(permutations)}\n")
        for permutation in permutations:
            writer.write(f"{' '.join([str(numb) for numb in permutation])}\n")


if __name__ == "__main__":
    permutation_int = parse_int(argv[1])
    combinations = [str(i) for i in range(1, permutation_int + 1)]
    report_combinations(find_combinations(5))
