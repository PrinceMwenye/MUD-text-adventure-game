from game import check_if_goal_attained
from unittest import TestCase


class TestIfGoalAttained(TestCase):
    def test_check_if_goal_attained_false(self):
        boss_health = 90
        actual = check_if_goal_attained(boss_health)
        expected = False
        self.assertEqual(expected, actual)

    def test_check_if_goal_attained_true(self):
        boss_health = 0
        actual = check_if_goal_attained(boss_health)
        expected = True
        self.assertEqual(expected, actual)

    def test_check_if_goal_attained_true_and_boss_health_below_zero(self):
        boss_health = -9
        actual = check_if_goal_attained(boss_health)
        expected = True
        self.assertEqual(expected, actual)