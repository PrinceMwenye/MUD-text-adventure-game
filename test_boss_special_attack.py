from game import boss_special_attack
from unittest import TestCase
from unittest.mock import patch
import io


class TestBossLaunchSpecialAttack(TestCase):
    @patch('random.randint', return_value=0)  # random number
    @patch('sys.stdout', new_callable=io.StringIO)  # if we are getting output
    def test_boss_special_attack_character_dictionary_changes(self, mock_stdout, mock_random_int):
        mock_character_before_attack = {'Current HP': 40}
        boss_special_attack(mock_character_before_attack)
        mock_character_after_attack = {'Current HP': 30}
        self.assertEqual(mock_character_before_attack, mock_character_after_attack)

    @patch('random.randint', return_value=0)  # random number
    @patch('sys.stdout', new_callable=io.StringIO)  # if we are getting output
    def test_boss_special_attack_first_mediocre_damage(self, mock_stdout, mock_random_int):
        mock_character_before_attack = {'Current HP': 40}
        boss_special_attack(mock_character_before_attack)
        mock_character_after_attack = {'Current HP': 30}
        self.assertEqual(mock_character_before_attack, mock_character_after_attack)

    @patch('random.randint', return_value=1)  # random number
    @patch('sys.stdout', new_callable=io.StringIO)  # if we are getting output
    def test_boss_special_attack_second_mediocre_damage(self, mock_stdout, mock_random_int):
        mock_character_before_attack = {'Current HP': 40}
        boss_special_attack(mock_character_before_attack)
        mock_character_after_attack = {'Current HP': 20}
        self.assertEqual(mock_character_before_attack, mock_character_after_attack)

    @patch('random.randint', return_value=2)  # random number
    @patch('sys.stdout', new_callable=io.StringIO)  # if we are getting output
    def test_boss_special_attack_third_deadly_damage(self, mock_stdout, mock_random_int):
        mock_character_before_attack = {'Current HP': 40}
        boss_special_attack(mock_character_before_attack)
        mock_character_after_attack = {'Current HP': 10}
        self.assertEqual(mock_character_before_attack, mock_character_after_attack)

    @patch('random.randint', return_value=3)  # random number
    @patch('sys.stdout', new_callable=io.StringIO)  # if we are getting output
    def test_boss_special_attack_fourth_deadly_damage(self, mock_stdout, mock_random_int):
        mock_character_before_attack = {'Current HP': 40}
        boss_special_attack(mock_character_before_attack)
        mock_character_after_attack = {'Current HP': 0}
        self.assertEqual(mock_character_before_attack, mock_character_after_attack)

