from game import make_board_descriptions
from unittest import TestCase
from unittest.mock import patch


class TestMakeBoardDescriptions(TestCase):
    @patch('random.randint', return_value=2)  # random number
    def test_make_board_descriptions_first_position_at_Zero_zero(self, _):
        mock_character = {'Current location': 'Maputo'}
        board = make_board_descriptions(25, 25, mock_character)[(0, 0)]
        expected = ("You look down.\n(._.)\nYou see animal footprints.Hmmm, something was here.\nBut remember, "
                    "animals "
                    "always come from behind. better be careful.\n"
                    "___________________________________________________________________\n")
        self.assertEqual(expected, board)

    @patch('random.randint', return_value=2)  # random number
    def test_make_board_descriptions_no_rows_no_columns(self, _):
        mock_character = {}
        board = make_board_descriptions(0, 0, mock_character)
        expected = {}
        self.assertEqual(expected, board)

    @patch('random.randint', return_value=2)  # random number
    def test_make_board_descriptions_dictionary_character_not_changed(self, _):
        initial_mock_character = {'Current location': 'Maputo',
                                  'Current level': 'Zulu',
                                  'Current_damage_points': 50}
        make_board_descriptions(0, 0, initial_mock_character)
        mock_character_after_function_invoked = {'Current location': 'Maputo',
                                                 'Current level': 'Zulu',
                                                 'Current_damage_points': 50}
        self.assertEqual(mock_character_after_function_invoked, initial_mock_character)
