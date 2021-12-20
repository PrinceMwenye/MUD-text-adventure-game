from game import make_board_map_zaire
from unittest import TestCase
from unittest.mock import patch


class TestMakeBoardMapZaire(TestCase):
    @patch('random.randint', return_value=1)  # random number
    @patch('random.randint', return_value=1)  # random number
    def test_make_board_map_zaire_giraffe(self, _, __):
        board = make_board_map_zaire(25, 25)[1][1]
        expected = '🦒'
        self.assertEqual(expected, board)

    @patch('random.randint', return_value=24)  # random number
    @patch('random.randint', return_value=20)  # random number
    def test_make_board_map_zaire_scar_at_fixed_position(self, _, __):
        board = make_board_map_zaire(25, 25)[24][20]
        expected = 'SCR'
        self.assertEqual(expected, board)
