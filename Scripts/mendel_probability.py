"""
Script to calculate the probability of an individual having a Dominant allele

Author: Dominique Massau
Date: 03/10/2020
"""


# imports
from sys import argv


# functions
def parse_numbers(text_file: str) -> tuple:
    """
    Parse the number of individuals with specific alleles

    Three numbers are given in a file on the same line (k, m and n). The
    number k represents homozygous dominant organisms, m represents
    heterozygous organisms and n represents homozygous recessive organisms
    The numbers are parsed from the first line of the file and returned
    in a tuple (in order: k, m. n)


    :param text_file: str, name of the text file
    :return: tuple, number of organisms with a specific allele
    """


def dominant_probability(individuals: tuple) -> float:
    """
    Calculate the probability of an individual having a dominant allele

    Based on the number of homozygous dominant individuals (k), the number of
    heterozygous organisms (m) and the number of homozygous recessive
    organisms (n) from the input, the probability is calculated that an
    organism has at least one dominant allele

    :param individuals: tuple, number of organisms with a specific allele
    :return: float, probability of an organism having a dominant allele
    """


if __name__ == "__main__":
    parse_numbers(argv[1])