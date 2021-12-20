from game import foe_run_away
from unittest import TestCase
from unittest.mock import patch


class TestFoeRunAway(TestCase):
    @patch('random.choices', return_value=[True])
    def test_foe_run_away_yes(self, _):
        character = {'Current HP': 40, 'xp': 10, 'Current_damage_points': 20}
        actual = foe_run_away(character)
        expected = True
        self.assertEqual(expected, actual)

    @patch('random.choices', return_value=[False])
    def test_foe_run_away_no(self, _):
        character = {'Current HP': 40, 'xp': 10, 'Current_damage_points': 20}
        actual = foe_run_away(character)
        expected = False
        self.assertEqual(expected, actual)

    @patch('random.choices', return_value=[False])
    def test_foe_run_away_no_dictionary_character_unchanged(self, _):
        initial_character = {'Current HP': 40, 'xp': 10, 'Current_damage_points': 20}
        mock_character_after_function_invoked = {'Current HP': 40, 'xp': 10, 'Current_damage_points': 20}
        foe_run_away(initial_character)
        self.assertEqual(mock_character_after_function_invoked, initial_character)

    @patch('random.choices', return_value=[True])
    def test_foe_run_away_yes_dictionary_changed(self, _):
        initial_character = {'Current HP': 40, 'xp': 10, 'Current_damage_points': 20}
        mock_character_after_function_invoked = {'Current HP': 40, 'xp': 20, 'Current_damage_points': 20}
        foe_run_away(initial_character)
        self.assertEqual(mock_character_after_function_invoked, initial_character)