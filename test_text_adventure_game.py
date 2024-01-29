import unittest
from unittest.mock import patch
from text_adventure import make_choice

class TestMakeChoice(unittest.TestCase):

    @patch('builtins.input', side_effect=['1'])
    def test_valid_choice(self, mock_input):
        choices = ["Option 1", "Option 2"]
        result = make_choice(choices)
        self.assertEqual(result, 1)

    @patch('builtins.input', side_effect=['3', '2'])
    def test_invalid_then_valid_choice(self, mock_input):
        choices = ["Option 1", "Option 2"]
        result = make_choice(choices)
        self.assertEqual(result, 2)

    @patch('builtins.input', side_effect=['invalid', '1'])
    def test_invalid_then_valid_input(self, mock_input):
        choices = ["Option 1", "Option 2"]
        result = make_choice(choices)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
