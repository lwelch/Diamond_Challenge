import unittest

from diamond_challenge import build_diamond, validate_input

class _DiamondChallengeUnitTest(unittest.TestCase):
    def test_valid_letter_A(self):
        self.assertEqual(validate_input('A'), True)
    def test_valid_letter_Z(self):
        self.assertEqual(validate_input('Z'), True)
    def test_valid_letter_M(self):
        self.assertEqual(validate_input('M'), True)
    def test_invalid_letter_q(self):
        self.assertEqual(validate_input('q'), False)
    def test_invalid_input_number(self):
        self.assertEqual(validate_input(1), False)
    def test_invalid_input_symbols(self):
        self.assertEqual(validate_input('.'), False)
        self.assertEqual(validate_input('!'), False)
        self.assertEqual(validate_input('*'), False)
    def test_invalid_input_edges(self):
        self.assertEqual(validate_input('@'), False)
        self.assertEqual(validate_input('['), False)
    def test_string_length_non_one(self):
        self.assertEqual(validate_input('Testfail'), False)
        self.assertEqual(validate_input('xy'), False)
        self.assertEqual(validate_input('Test space'), False)
    def test_simple_diamond(self):
        test_list = [
            '  A',
            ' B B',
            'C   C',
            ' B B',
            '  A'
        ]
        self.assertLessEqual(build_diamond('C'), test_list)
    def test_A_input(self):
        test_list = [
            'A'
        ]
        self.assertLessEqual(build_diamond('A'), test_list)

