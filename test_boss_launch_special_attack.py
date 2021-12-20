from game import boss_launch_special_attack
from unittest import TestCase
from unittest.mock import patch


class TestBossLaunchSpecialAttack(TestCase):
    @patch('random.choices', return_value=[True])  # random choice
    def test_boss_launch_special_attack_true(self, _):
        actual = boss_launch_special_attack()
        expected = True
        self.assertEqual(expected, actual)

    @patch('random.choices', return_value=[False])  # random choice
    def test_boss_launch_special_attack_false(self, _):
        actual = boss_launch_special_attack()
        expected = False
        self.assertEqual(expected, actual)
