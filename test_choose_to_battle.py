from game import choose_to_battle
from unittest import TestCase
from unittest.mock import patch
import io
from colorama import Fore, Style


class TestChooseToBattle(TestCase):
    @patch('builtins.input', side_effect=['y'])  # user input
    def test_choose_to_battle_yes(self, mock_input):
        actual = choose_to_battle()
        expected = True
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['n'])  # user input
    def test_choose_to_battle_no(self, mock_input):
        actual = choose_to_battle()
        expected = False
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['wrong', 'n'])  # user input
    @patch('sys.stdout', new_callable=io.StringIO)  # if we are getting output
    def test_choose_to_battle_invalid_choice(self, mock_std_out, mock_input):
        choose_to_battle()
        game_printed_this = mock_std_out.getvalue()
        expected = ('____________________________________________________________________\n' +
                    Fore.RED + "Invalid choice. Valid_choices are\n[y to fight or n to not fight]" + Style.RESET_ALL
                    + "\n")

        self.assertEqual(expected, game_printed_this)
