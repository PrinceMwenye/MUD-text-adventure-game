from game import recuperate
from unittest import TestCase
from unittest.mock import patch
import io
from colorama import Fore, Style


class TestRecuperate(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)  # if we are getting output
    def test_recuperate_character_dying(self, mock_stdout):
        mock_character = {'Current HP': 5}
        recuperate(mock_character)
        game_printed_this = mock_stdout.getvalue()
        expected = (
                Fore.BLUE + "Not sure you can make it to Zamunda with this health. You pray to the gods for help.\nThey"
                            " hear you!.The gods increase your HP by 20" + Style.RESET_ALL + "\n")
        self.assertEqual(expected, game_printed_this)

    def test_recuperate_character_dictionary_changed_when_Current_HP_less_than_eleven(self):
        mock_character = {'Current HP': 5}
        recuperate(mock_character)
        expected = {'Current HP': 25}
        self.assertEqual(expected, mock_character)

    def test_recuperate_character_dictionary_unchanged_when_current_HP_more_than_ten(self):
        initial_mock_character = {'Current HP': 25}
        mock_character_after_function_invoked = {'Current HP': 25}
        recuperate(initial_mock_character)
        self.assertEqual(mock_character_after_function_invoked, initial_mock_character)
