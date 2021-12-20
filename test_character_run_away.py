from game import character_run_away
from unittest import TestCase
from unittest.mock import patch
import io
from colorama import Fore, Style


class TestCharacterRunAway(TestCase):
    @patch('random.randint', return_value=20)  # random number
    @patch('random.choices', return_value=[True])  # random number
    @patch('sys.stdout', new_callable=io.StringIO)  # if we are getting output
    def test_character_damaged_output(self, mock_stdout, _, __):
        character = {'class_attributes': {'levels': ['novice', 'soldier', 'ultimate']},
                     'Current level': 'novice', 'Current HP': 40}
        character_run_away(character)
        expected = (Fore.YELLOW + "It is risky to turn your back on a foe." + Style.RESET_ALL + "\n" +
                    u"\u001b[31;1mAs you turn your back, foe scratches you. Ouch! that cost 5 health points\u001b[0m\n"
                    )
        game_printed_this = mock_stdout.getvalue()
        self.assertEqual(expected, game_printed_this)

    @patch('random.randint', return_value=20)  # random number
    @patch('random.choices', return_value=[False])  # random number
    @patch('sys.stdout', new_callable=io.StringIO)  # if we are getting output
    def test_character_not_damaged_output(self, mock_stdout, _, __):
        character = {'class_attributes': {'levels': ['novice', 'soldier', 'ultimate']},
                     'Current level': 'novice'}
        character_run_away(character)
        expected = (Fore.YELLOW + "It is risky to turn your back on a foe." + Style.RESET_ALL + "\n" +
                    "\u001b[34;1mYou get away with it this time\u001b[0m\n"
                    )
        game_printed_this = mock_stdout.getvalue()
        self.assertEqual(expected, game_printed_this)

    @patch('random.randint', return_value=20)  # random number
    @patch('random.choices', return_value=[True])  # random number
    @patch('sys.stdout', new_callable=io.StringIO)  # if we are getting output
    def test_character_damaged_current_HP_reduced(self, _, __, ___):
        character = {'class_attributes': {'levels': ['novice', 'soldier', 'ultimate']},
                     'Current level': 'novice', 'Current HP': 50}
        character_run_away(character)
        expected_character_current_hp = 45
        self.assertEqual(expected_character_current_hp, character['Current HP'])

    @patch('random.randint', return_value=20)  # random number
    @patch('random.choices', return_value=[False])  # random number
    @patch('sys.stdout', new_callable=io.StringIO)  # if we are getting output
    def test_character_not_damaged_dictionary_not_changed(self, _, __, ___):
        initial_character = {'class_attributes': {'levels': ['novice', 'soldier', 'ultimate']},
                             'Current level': 'novice', 'Current HP': 50}
        mock_character_after_function_invoked = {'class_attributes': {'levels': ['novice', 'soldier', 'ultimate']},
                                                 'Current level': 'novice', 'Current HP': 50}
        character_run_away(initial_character)
        self.assertEqual(mock_character_after_function_invoked, initial_character)
