from game import check_for_foes
from unittest import TestCase
from unittest.mock import patch


class TestCheckForFoes(TestCase):
    @patch('random.choices', return_value=[True])
    def test_check_for_foes_find_foe(self, _):
        actual = check_for_foes()
        expected = True
        self.assertEqual(expected, actual)

    @patch('random.choices', return_value=[False])
    def test_check_for_foes_no_foe_available(self, _):
        actual = check_for_foes()
        expected = False
        self.assertEqual(expected, actual)
