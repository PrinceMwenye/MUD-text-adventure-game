from game import check_if_character_is_damaged
from unittest import TestCase
from unittest.mock import patch


class TestCheckIfCharacterIsDamaged(TestCase):
    @patch('random.choices', return_value=[False])  # random choice
    def test_foe_run_away_no(self, mock_random_choice):
        actual = check_if_character_is_damaged()
        expected = False
        self.assertEqual(expected, actual)

    @patch('random.choices', return_value=[True])  # random choice
    def test_foe_run_away_yes(self, mock_random_choice):
        actual = check_if_character_is_damaged()
        expected = True
        self.assertEqual(expected, actual)
