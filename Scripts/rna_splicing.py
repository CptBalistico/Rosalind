"""
Script to excise intronic sequences from DNA and translate it to a protein

Author: Dominique Massau
Date: 29/09/2020
"""

# imports
from sys import argv


# functions
def parse_fastas(text_file: str) -> list:
    """
    Parse a main DNA sequence and intronic sub sequences

    :param text_file: str, name of file containing fasta's
    :return: list, main sequence at index 0 and sub sequences
    """


def excise_introns(sequences: list) -> str:
    """
    Excise intronic subs sequences from the main DNA sequence

    :param sequences: list,  main sequence at index 0 and sub sequences
    :return: str, DNA sequences without intronic sequences
    """



if __name__ == "__main__":
    fasta_list = parse_fastas(argv[1])