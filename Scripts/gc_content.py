"""
Compute the GC content and report the sequence with the highest content

Author: Dominique Massau
"""

# imports
from sys import argv


# functions
def parse_fasta(file_name: str) -> dict:
    """
    Parse a fasta file into a dictionary

    :param file_name: str, name of the fasta file
    :return: dict, contains fasta header: sequence
    """

    with open(file_name, 'r') as lines:
        fasta_dict = {}
        for line in lines:
            if line.startswith('>'):
                current_header = line.strip('>').strip()
                fasta_dict[current_header] = []
            else:
                fasta_dict[current_header].append(line.strip())

    for header, seq in fasta_dict.items():
        fasta_dict[header] = ''.join(seq)
    return fasta_dict


if __name__ == "__main__":
    print(parse_fasta(argv[1]))
