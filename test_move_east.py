from game import move_east, make_board_map_maputo
from unittest import TestCase
from unittest.mock import patch
import io


class TestMoveEast(TestCase):
    @patch('random.randint', return_value=0)  # random number
    @patch('sys.stdout', new_callable=io.StringIO)  # if we are getting output
    def test_move_east_animal_behind(self, _, __):
        mock_character = {'X-coordinate': 0, 'Y-coordinate': 0, 'xp': 10}
        mock_board = make_board_map_maputo(25, 25)
        move_east(mock_character, mock_board)
        expected_character_after_move = {'X-coordinate': 1, 'Y-coordinate': 0, 'xp': 35}
        self.assertEqual(expected_character_after_move, mock_character)

    @patch('random.randint', return_value=0)  # random number
    @patch('sys.stdout', new_callable=io.StringIO)  # if we are getting output
    def test_move_east_animal_behind_message_printed(self, mock_stdout, _):
        mock_character = {'X-coordinate': 0, 'Y-coordinate': 0, 'xp': 20}
        mock_board = make_board_map_maputo(25, 25)
        expected = (
            '\u001b[32;1mAnimals sneak from behind. As you move East An animal looms behind you. You turn around '
            'and smash the animal. It tastes good!\u001b[0m.\n'
        )
        move_east(mock_character, mock_board)
        game_printed_this = mock_stdout.getvalue()
        self.assertEqual(expected, game_printed_this)

    @patch('random.randint', return_value=1)  # random number
    @patch('sys.stdout', new_callable=io.StringIO)  # if we are getting output
    def test_move_east_no_animal_behind(self, mock_stdout, _):
        mock_character = {'X-coordinate': 0, 'Y-coordinate': 0, 'xp': 20}
        mock_board = make_board_map_maputo(25, 25)
        move_east(mock_character, mock_board)
        expected_character_after_move = {'X-coordinate': 1, 'Y-coordinate': 0, 'xp': 20}
        self.assertEqual(expected_character_after_move, mock_character)

    @patch('random.randint', return_value=3)  # animal at board[3][3]
    @patch('sys.stdout', new_callable=io.StringIO)  # if we are getting output
    def test_move_east_no_animal_behind_no_increased_xp(self, mock_stdout, _):
        mock_character = {'X-coordinate': 1, 'Y-coordinate': 0, 'xp': 20}
        mock_board = make_board_map_maputo(25, 25)
        move_east(mock_character, mock_board)
        expected_character_after_move = {'X-coordinate': 2, 'Y-coordinate': 0, 'xp': 20}
        self.assertEqual(expected_character_after_move, mock_character)



