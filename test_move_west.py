from game import move_west, make_board_map_maputo
from unittest import TestCase
from unittest.mock import patch
import io


class TestMoveEast(TestCase):
    @patch('random.randint', return_value=1)  # random number
    @patch('random.randint', return_value=1)  # random number
    @patch('sys.stdout', new_callable=io.StringIO)  # if we are getting output
    def test_move_west_animal_behind(self, _, __, ___):
        mock_character = {'X-coordinate': 1, 'Y-coordinate': 0, 'xp': 10}
        mock_board = make_board_map_maputo(25, 25)
        move_west(mock_character, mock_board)
        expected_character_after_move = {'X-coordinate': 0, 'Y-coordinate': 0, 'xp': 10}
        self.assertEqual(expected_character_after_move, mock_character)

    @patch('random.randint', return_value=3)  # random number
    @patch('sys.stdout', new_callable=io.StringIO)  # if we are getting output
    def test_move_west_no_animal_behind(self, mock_stdout, _):
        mock_character = {'X-coordinate': 2, 'Y-coordinate': 0, 'xp': 20}
        mock_board = make_board_map_maputo(25, 25)
        move_west(mock_character, mock_board)
        expected_character_after_move = {'X-coordinate': 1, 'Y-coordinate': 0, 'xp': 20}
        self.assertEqual(expected_character_after_move, mock_character)

    @patch('random.randint', return_value=3)  # animal at board[3][3]
    @patch('sys.stdout', new_callable=io.StringIO)  # if we are getting output
    def test_move_west_no_animal_behind_no_increased_xp(self, mock_stdout, _):
        mock_character = {'X-coordinate': 1, 'Y-coordinate': 0, 'xp': 20}
        mock_board = make_board_map_maputo(25, 25)
        move_west(mock_character, mock_board)
        expected_character_after_move = {'X-coordinate': 0, 'Y-coordinate': 0, 'xp': 20}
        self.assertEqual(expected_character_after_move, mock_character)
