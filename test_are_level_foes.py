from game import area_level_foes
from unittest import TestCase
from unittest.mock import patch


class TestLevelFoes(TestCase):
    @patch('random.randint', return_value=0)  # random number
    def test_foes_level_zero_maputo_area(self, _):  # level 0 (second level is the boss)
        character = {'class_attributes': {'levels': ['novice', 'soldier', 'ultimate']},
                     'Current level': 'novice'}
        actual = area_level_foes(character)
        expected = ('Timon_tribe', 'GLAGWA')
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=0)  # random number
    def test_foes_level_zero_area_zaire(self, _):  # level one (second level is the boss)
        character = {'class_attributes': {'levels': ['novice', 'soldier', 'ultimate']},
                     'Current level': 'soldier'}
        actual = area_level_foes(character)
        expected = ('Nala_tribe', 'SPEAR')
        self.assertEqual(expected, actual)

    def test_foes_area_level_dictionary_not_changed(self):
        initial_character = {'class_attributes': {'levels': ['novice', 'soldier', 'ultimate']},
                             'Current level': 'soldier'}
        character_after_function_invoked = {'class_attributes': {'levels': ['novice', 'soldier', 'ultimate']},
                                            'Current level': 'soldier'}
        area_level_foes(initial_character)
        self.assertEqual(character_after_function_invoked, initial_character)
