from unittest import TestCase
from Scripts.dna_to_rna import convert_dna_to_rna


class TestDnaToRna(TestCase):

    # Test general functionality
    def test_covert_dna_to_rna_correct(self):
        outcome = convert_dna_to_rna("ACGTTCTACCT")
        self.assertEqual(outcome, "ACGUUCUACCU", "Supposed to to be ACGUUCUACCU")

    # Test short sequences
    def test_covert_dna_to_rna_short(self):
        outcome = convert_dna_to_rna("AT")
        self.assertEqual(outcome, "AU", "Supposed to to be AU")

    # Test if ValueError is raised if spaces are included
    def test_convert_dna_to_rna_spaces(self):
        with self.assertRaises(ValueError):
            convert_dna_to_rna("ACGTTC  TA  CCT ")

    # Test is ValueError is raised if invalid characters are included
    def test_convert_dna_to_rna_unknown_char(self):
        with self.assertRaises(ValueError):
            convert_dna_to_rna("ACTGKK8Z")

    # Test is ValueError is raised if an empty string is given
    def test_convert_dna_to_rna_unknown_empty(self):
        with self.assertRaises(ValueError):
            convert_dna_to_rna("")
