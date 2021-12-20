from game import update_character_level
from unittest import TestCase


class TestUpdateCharacterLevel(TestCase):
    def test_update_character_level_to_level_one_hunter_class(self):
        mock_character = {'class_attributes': {'levels': ['Bantu', 'Zulu', 'Masai'],
                                               'special_attack': 'knobkerrie',
                                               'max_damage_points': [('Bantu', 40), ('Zulu', 50),
                                                                     ('Masai', 55)],
                                               'max_Current_HP': [('Bantu', 50), ('Zulu', 70), ('Masai', 80)],
                                               'experience_to_next_level': {'Zulu': 400, 'Masai': 600}},
                          'xp': 450, 'location levels': ['Maputo', 'Zaire', 'Zamunda'],
                          'Current HP': 50,
                          'Current level': 'Bantu',
                          'Current location': 'Maputo',
                          'Current_damage_points': 40,
                          }

        actual = update_character_level(mock_character)
        expected = {'Current HP': 70,
                    'Current level': 'Zulu',
                    'Current location': 'Zaire',
                    'Current_damage_points': 50,
                    'class_attributes': {'experience_to_next_level': {'Zulu': 400,
                                                                      'Masai': 600},
                                         'levels': ['Bantu', 'Zulu', 'Masai'],
                                         'max_Current_HP': [('Bantu', 50),
                                                            ('Zulu', 70),
                                                            ('Masai', 80)],
                                         'max_damage_points': [('Bantu', 40),
                                                               ('Zulu', 50),
                                                               ('Masai', 55)],
                                         'special_attack': 'knobkerrie'},
                    'location levels': ['Maputo', 'Zaire', 'Zamunda'],
                    'xp': 450}
        self.assertEqual(expected, actual)
