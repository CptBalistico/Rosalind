"""
Script to calculate the probability of an individual having a Dominant allele

Author: Dominique Massau
Date: 03/10/2020
"""


# imports
from sys import argv


# functions
def parse_numbers(text_file: str) -> list:
    """
    Parse the number of individuals with specific alleles

    Three numbers are given in a file on the same line (k m n). The
    number k represents homozygous dominant organisms, m represents
    heterozygous organisms and n represents homozygous recessive organisms
    The numbers are parsed from the first line of the file and returned
    in a tuple (in order: k, m, n)

    :param text_file: str, name of the text file
    :return: list, number of organisms with a specific allele
    """

    with open(text_file, 'r') as lines:
        for line in lines:
            if line.strip() == '':
                continue
            else:
                return [int(number) for number in line.split(' ')]


def dominant_probability(individuals: list) -> float:
    """
    Calculate the probability of an individual having a dominant allele

    Based on the number of homozygous dominant individuals (k), the number of
    heterozygous organisms (m) and the number of homozygous recessive
    organisms (n) from the input, the probability is calculated that an
    organism has at least one dominant allele

    :param individuals: list, number of organisms with a specific allele
    :return: float, probability of an organism having a dominant allele
    """

    total = sum(individuals)
    h_dom, het, h_rec = individuals[0], individuals[1], individuals[2]
    probabilities = []

    # AA * AA
    probabilities.append(h_dom / total * (h_dom - 1) / (total - 1))
    # AA * Aa
    probabilities.append(h_dom / total * (het / (total - 1)))
    # AA * aa
    probabilities.append(h_dom / total * (h_rec / (total - 1)))

    # Aa * AA
    probabilities.append(het / total * (h_dom / (total - 1)))
    # Aa * Aa
    probabilities.append((het / total * (het - 1) / (total - 1)) * 0.75)
    # Aa * aa
    probabilities.append(het / total * (h_rec / (total - 1)) * 0.50)

    # aa * AA
    probabilities.append(h_rec / total * (h_dom / (total - 1)))
    # aa * Aa
    probabilities.append(h_rec / total * (het / (total - 1)) * 0.5)

    return sum(probabilities)


if __name__ == "__main__":
    numbers = parse_numbers(argv[1])
    print(dominant_probability(numbers))
