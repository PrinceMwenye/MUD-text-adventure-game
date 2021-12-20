from unittest import TestCase
from unittest.mock import patch
from game import get_user_choice
import io
from colorama import Fore, Style


class TestGetUserChoice(TestCase):
    @patch('builtins.input', side_effect=['d'])  # user input
    def test_user_choice_east(self, _):
        self.assertEqual('East', get_user_choice())

    @patch('builtins.input', side_effect=['a'])  # user input
    def test_user_choice_west(self, _):
        self.assertEqual('West', get_user_choice())

    @patch('builtins.input', side_effect=['w'])  # user input
    def test_user_choice_north(self, _):
        self.assertEqual('North', get_user_choice())

    @patch('builtins.input', side_effect=['s'])  # user input
    def test_user_choice_south(self, _):
        self.assertEqual('South', get_user_choice())

    @patch('builtins.input', side_effect=['sf', 's'])  # user input
    @patch('sys.stdout', new_callable=io.StringIO)  # if we are getting output
    def test_user_choice_invalid_input_then_valid(self, mock_stdout, _):
        get_user_choice()
        expected = (
                Fore.RED + 'Invalid direction, only possible directions are ["d for East", "a for West", "w for North",'
                           '"s for South"]' + Style.RESET_ALL
        )
        message_printed = mock_stdout.getvalue()
        self.assertTrue(expected in message_printed)
