from game import describe_current_location, make_board_descriptions
from unittest import TestCase
from unittest.mock import patch
import io
from colorama import Fore, Style


class TestDescribeCurrentLocation(TestCase):
    @patch('random.randint', return_value=4)  # random number
    @patch('sys.stdout', new_callable=io.StringIO)  # if we are getting output
    def test_describe_current_location_maputo(self, std_output, _):
        mock_character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5, 'Current location': 'Maputo'}
        board = make_board_descriptions(25, 25, mock_character)
        describe_current_location(mock_character, board)
        actual = std_output.getvalue()
        expected = ("You are at (0, 0)\nHere lie the remains of an elephant. You wonder which tribe hunted it. Or "
                    "which animal.\nYou pick "
                    "a bone which might be useful later and put it in your bag.\nYou light up a cigarette."
                    "  (̅_̅_̅_̅(̅_̅_̅_̅_̅_̅_̅_̅_̅̅_̅()\n'Rest Bafethu', you hear the wind whisper\n"
                    "___________________________________________________________________\n" + "\n")
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=0)  # random number
    @patch('sys.stdout', new_callable=io.StringIO)  # if we are getting output
    def test_describe_current_location_zaire(self, std_output, _):
        mock_character = {'X-coordinate': 2, 'Y-coordinate': 2, 'Current HP': 5, 'Current location': 'Zaire'}
        board = make_board_descriptions(25, 25, mock_character)
        describe_current_location(mock_character, board)
        actual = std_output.getvalue()
        expected = ("You are at (2, 2)\nYou see a sign. It says 'MUFASA_TRIBE'.\n" + Fore.RED + "➶➶➶➶➶ƭεรƭ➷➷➷➷➷"
                    + Style.RESET_ALL +
                    "This gives you shivers. But you are brave.\nbThe sun is setting. Maybe you need some rest?\n"
                    "___________________________________________________________________\n" + "\n")
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=2)  # random number
    def test_describe_current_location_character_not_changed(self, _):
        initial_mock_character = {'Current location': 'Maputo',
                                  'Current level': 'Zulu',
                                  'Current_damage_points': 50,
                                  'X-coordinate': 2,
                                  'Y-coordinate': 2}
        board_description = {(2, 2): "You are enjoying Unit Testing"}
        describe_current_location(initial_mock_character, board_description)
        mock_character_after_function_invoked = {'Current location': 'Maputo',
                                                 'Current level': 'Zulu',
                                                 'Current_damage_points': 50,
                                                 'X-coordinate': 2, 'Y-coordinate': 2}
        self.assertEqual(mock_character_after_function_invoked, initial_mock_character)
