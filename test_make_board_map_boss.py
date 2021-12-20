from game import make_board_map_boss
from unittest import TestCase
from unittest.mock import patch


class TestMakeBoardMapBoss(TestCase):
    @patch('random.randint', return_value=1)  # random number
    @patch('random.randint', return_value=1)  # random number
    def test_make_board_map_boss_elephant(self, _, __):
        board = make_board_map_boss(25, 25)[1][1]
        expected = '\u001b[34m🐘\u001b[0m'
        self.assertEqual(expected, board)

    @patch('random.randint', return_value=24)  # random number
    @patch('random.randint', return_value=20)  # random number
    def test_make_board_map_boss_scar_at_fixed_position_emoji_appears(self, _, __):
        board = make_board_map_boss(25, 25)[24][20]
        expected = '🦁'
        self.assertEqual(expected, board)

    def test_make_board_map_boss_area_near_Scar_and_character_empty(self):
        board = make_board_map_boss(25, 25)[23][21]
        expected = ''
        self.assertEqual(expected, board)
