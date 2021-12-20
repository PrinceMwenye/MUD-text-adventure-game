from unittest import TestCase
from game import check_if_alive
import io
from unittest.mock import patch


class TestCheckIfAlive(TestCase):
    def test_check_if_alive_zero_HP(self):
        character = {'X-coordinate': 3, 'Y-coordinate': 0, 'Current HP': 0}
        expected = False
        actual = check_if_alive(character)
        self.assertEqual(expected, actual)

    def test_check_if_alive_greater_than_zero_HP(self):
        character = {'X-coordinate': 3, 'Y-coordinate': 0, 'Current HP': 1}
        expected = True
        actual = check_if_alive(character)
        self.assertEqual(expected, actual)

    def test_check_if_alive_true_dictionary_character_unchanged(self):
        original_character = {'X-coordinate': 3, 'Y-coordinate': 0, 'Current HP': 1}
        original_character_copy = {'X-coordinate': 3, 'Y-coordinate': 0, 'Current HP': 1}
        check_if_alive(original_character)
        self.assertEqual(original_character, original_character_copy)

    def test_check_if_alive_false_dictionary_character_unchanged(self):
        original_character = {'X-coordinate': 3, 'Y-coordinate': 0, 'Current HP': 0}
        original_character_copy = {'X-coordinate': 3, 'Y-coordinate': 0, 'Current HP': 0}
        check_if_alive(original_character)
        self.assertEqual(original_character, original_character_copy)

    @patch('sys.stdout', new_callable=io.StringIO)  # if we are getting output
    def test_check_if_alive_more_than_30_HP(self, mock_stdout):
        character = {'Current HP': 31}
        check_if_alive(character)
        game_printed_this = mock_stdout.getvalue()
        expected_output = "Health-wise, you seem to be ok\n"
        self.assertEqual(expected_output, game_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)  # if we are getting output
    def test_check_if_alive_less_than_30_HP(self, mock_stdout):
        character = {'Current HP': 29}
        check_if_alive(character)
        game_printed_this = mock_stdout.getvalue()
        expected_output = "You bleed heavily\n"
        self.assertTrue(expected_output, game_printed_this)
