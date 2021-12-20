from game import check_new_level_attained
from unittest import TestCase


class TestCheckNewLevelAttained(TestCase):
    def test_new_level_attained_to_level_one_true(self):  # Zaire level
        mock_character = {'class_attributes': {'levels': ['tinkerbell', 'vampire', 'witcher'],
                                               'special_attack': 'magic',
                                               'max_damage_points': [('tinkerbell', 40), ('vampire', 50),
                                                                     ('witcher', 55)],
                                               'max_Current_HP': [('tinkerbell', 50), ('vampire', 70), ('witcher', 80)],
                                               'experience_to_next_level': {'vampire': 450, 'witcher': 675}},
                          'Current level': 'tinkerbell',
                          'xp': 450}

        actual = check_new_level_attained(mock_character)
        expected = True
        self.assertEqual(expected, actual)

    def test_new_level_attained_yes_dictionary_not_changed(self):  # Zaire level
        mock_character = {'class_attributes': {'levels': ['tinkerbell', 'vampire', 'witcher'],
                                               'special_attack': 'magic',
                                               'max_damage_points': [('tinkerbell', 40), ('vampire', 50),
                                                                     ('witcher', 55)],
                                               'max_Current_HP': [('tinkerbell', 50), ('vampire', 70), ('witcher', 80)],
                                               'experience_to_next_level': {'vampire': 450, 'witcher': 675}},
                          'Current level': 'tinkerbell',
                          'xp': 450}

        mock_character_after_function_invoked = {'class_attributes': {'levels': ['tinkerbell', 'vampire', 'witcher'],
                                                                      'special_attack': 'magic',
                                                                      'max_damage_points': [('tinkerbell', 40),
                                                                                            ('vampire', 50),
                                                                                            ('witcher', 55)],
                                                                      'max_Current_HP': [('tinkerbell', 50),
                                                                                         ('vampire', 70),
                                                                                         ('witcher', 80)],
                                                                      'experience_to_next_level': {'vampire': 450,
                                                                                                   'witcher': 675}},
                                                 'Current level': 'tinkerbell',
                                                 'xp': 450}

        check_new_level_attained(mock_character)
        self.assertEqual(mock_character, mock_character_after_function_invoked)

    def test_new_level_attained_to_level_one_false(self):  # Zaire level
        mock_character = {'class_attributes': {'levels': ['tinkerbell', 'vampire', 'witcher'],
                                               'special_attack': 'magic',
                                               'max_damage_points': [('tinkerbell', 40), ('vampire', 50),
                                                                     ('witcher', 55)],
                                               'max_Current_HP': [('tinkerbell', 50), ('vampire', 70), ('witcher', 80)],
                                               'experience_to_next_level': {'vampire': 450, 'witcher': 675}},
                          'Current level': 'tinkerbell',
                          'xp': 400}

        actual = check_new_level_attained(mock_character)
        expected = False
        self.assertEqual(expected, actual)

    def test_new_level_attained_no_dictionary_not_changed(self):  # Zaire level
        mock_character = {'class_attributes': {'levels': ['tinkerbell', 'vampire', 'witcher'],
                                               'special_attack': 'magic',
                                               'max_damage_points': [('tinkerbell', 40), ('vampire', 50),
                                                                     ('witcher', 55)],
                                               'max_Current_HP': [('tinkerbell', 50), ('vampire', 70), ('witcher', 80)],
                                               'experience_to_next_level': {'vampire': 450, 'witcher': 675}},
                          'Current level': 'tinkerbell',
                          'xp': 20}

        mock_character_after_function_invoked = {'class_attributes': {'levels': ['tinkerbell', 'vampire', 'witcher'],
                                                                      'special_attack': 'magic',
                                                                      'max_damage_points': [('tinkerbell', 40),
                                                                                            ('vampire', 50),
                                                                                            ('witcher', 55)],
                                                                      'max_Current_HP': [('tinkerbell', 50),
                                                                                         ('vampire', 70),
                                                                                         ('witcher', 80)],
                                                                      'experience_to_next_level': {'vampire': 450,
                                                                                                   'witcher': 675}},
                                                 'Current level': 'tinkerbell',
                                                 'xp': 20}

        check_new_level_attained(mock_character)
        self.assertEqual(mock_character, mock_character_after_function_invoked)
