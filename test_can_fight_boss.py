from game import can_fight_boss
from unittest import TestCase


class TestCanFightBoss(TestCase):
    def test_can_fight_boss_true(self):
        mock_character = {'class_attributes': {'levels': ['Bantu', 'Zulu', 'Masai'],
                                               'special_attack': 'knobkerrie',
                                               'max_damage_points': [('Bantu', 40), ('Zulu', 50),
                                                                     ('Masai', 55)],
                                               'max_Current_HP': [('Bantu', 50), ('Zulu', 70),
                                                                  ('Masai', 80)],
                                               'experience_to_next_level': {'Zulu': 400,
                                                                            'Masai': 600}},
                          'xp': 450, 'location levels': ['Maputo', 'Zaire', 'Zamunda'],
                          'Current HP': 50,
                          'Current level': 'Masai',
                          'Current location': 'Zamunda',
                          'Current_damage_points': 40,
                          }

        actual = can_fight_boss(mock_character)
        expected = True
        self.assertEqual(expected, actual)

    def test_can_fight_boss_false(self):
        mock_character = {'class_attributes': {'levels': ['Bantu', 'Zulu', 'Masai'],
                                               'special_attack': 'knobkerrie',
                                               'max_damage_points': [('Bantu', 40), ('Zulu', 50),
                                                                     ('Masai', 55)],
                                               'max_Current_HP': [('Bantu', 50), ('Zulu', 70),
                                                                  ('Masai', 80)],
                                               'experience_to_next_level': {'Zulu': 400,
                                                                            'Masai': 600}},
                          'xp': 450, 'location levels': ['Maputo', 'Zaire', 'Zamunda'],
                          'Current HP': 50,
                          'Current level': 'Bantu',
                          'Current location': 'Zamunda',
                          'Current_damage_points': 40,
                          }
        actual = can_fight_boss(mock_character)
        expected = False
        self.assertEqual(expected, actual)

    def test_can_fight_boss_false_dictionary_not_changed(self):
        initial_mock_character = {'class_attributes': {'levels': ['Bantu', 'Zulu', 'Masai'],
                                                       'special_attack': 'knobkerrie',
                                                       'max_damage_points': [('Bantu', 40), ('Zulu', 50),
                                                                             ('Masai', 55)],
                                                       'max_Current_HP': [('Bantu', 50), ('Zulu', 70),
                                                                          ('Masai', 80)],
                                                       'experience_to_next_level': {'Zulu': 400,
                                                                                    'Masai': 600}},
                                  'xp': 450, 'location levels': ['Maputo', 'Zaire', 'Zamunda'],
                                  'Current HP': 50,
                                  'Current level': 'Bantu',
                                  'Current location': 'Zamunda',
                                  'Current_damage_points': 40,
                                  }

        mock_character_after_function_invoked = {'class_attributes': {'levels': ['Bantu', 'Zulu', 'Masai'],
                                                                      'special_attack': 'knobkerrie',
                                                                      'max_damage_points': [('Bantu', 40), ('Zulu', 50),
                                                                                            ('Masai', 55)],
                                                                      'max_Current_HP': [('Bantu', 50), ('Zulu', 70),
                                                                                         ('Masai', 80)],
                                                                      'experience_to_next_level': {'Zulu': 400,
                                                                                                   'Masai': 600}},
                                                 'xp': 450, 'location levels': ['Maputo', 'Zaire', 'Zamunda'],
                                                 'Current HP': 50,
                                                 'Current level': 'Bantu',
                                                 'Current location': 'Zamunda',
                                                 'Current_damage_points': 40,
                                                 }
        can_fight_boss(initial_mock_character)
        self.assertEqual(mock_character_after_function_invoked, initial_mock_character)

    def test_can_fight_boss_true_dictionary_not_changed(self):
        initial_mock_character = {'class_attributes': {'levels': ['Bantu', 'Zulu', 'Masai'],
                                                       'special_attack': 'knobkerrie',
                                                       'max_damage_points': [('Bantu', 40),
                                                                             ('Zulu', 50),
                                                                             ('Masai', 55)],
                                                       'max_Current_HP': [('Bantu', 50), ('Zulu', 70),
                                                                          ('Masai', 80)],
                                                       'experience_to_next_level': {'Zulu': 400,
                                                                                    'Masai': 600}},
                                  'xp': 450, 'location levels': ['Maputo', 'Zaire', 'Zamunda'],
                                  'Current HP': 50,
                                  'Current level': 'Masai',
                                  'Current location': 'Zamunda',
                                  'Current_damage_points': 40,
                                  }

        mock_character_after_function_invoked = {'class_attributes': {'levels': ['Bantu', 'Zulu', 'Masai'],
                                                                      'special_attack': 'knobkerrie',
                                                                      'max_damage_points': [('Bantu', 40), ('Zulu', 50),
                                                                                            ('Masai', 55)],
                                                                      'max_Current_HP': [('Bantu', 50), ('Zulu', 70),
                                                                                         ('Masai', 80)],
                                                                      'experience_to_next_level': {'Zulu': 400,
                                                                                                   'Masai': 600}},
                                                 'xp': 450, 'location levels': ['Maputo', 'Zaire', 'Zamunda'],
                                                 'Current HP': 50,
                                                 'Current level': 'Masai',
                                                 'Current location': 'Zamunda',
                                                 'Current_damage_points': 40,
                                                 }
        can_fight_boss(initial_mock_character)
        self.assertEqual(mock_character_after_function_invoked, initial_mock_character)
