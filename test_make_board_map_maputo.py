from game import make_board_map_maputo
from unittest import TestCase
from unittest.mock import patch


class TestMakeBoardMapMaputo(TestCase):
    @patch('random.randint', return_value=1)  # random number
    @patch('random.randint', return_value=1)  # random number
    def test_make_board_elephant_at_position_one_one(self, _, __):
        board = make_board_map_maputo(25, 25)[1][1]
        expected = '\u001b[34m🐘\u001b[0m'
        self.assertEqual(expected, board)

    @patch('random.randint', return_value=24)  # random number
    @patch('random.randint', return_value=20)  # random number
    def test_make_board_map_maputo_scar_at_fixed_position(self, _, __):
        board = make_board_map_maputo(25, 25)[24][20]
        expected = 'SCR'
        self.assertEqual(expected, board)
