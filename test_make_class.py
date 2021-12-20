from game import make_class
from unittest import TestCase


class TestMakeClass(TestCase):
    def test_make_class(self):
        actual = make_class()
        expected = {'fighter': {'levels': ['novice', 'soldier', 'ultimate'],
                                'special_attack': 'sword',
                                'max_damage_points': [('novice', 20), ('soldier', 30), ('ultimate', 40)],
                                'max_Current_HP': [('novice', 50), ('soldier', 70), ('ultimate', 80)],
                                'experience_to_next_level': {'soldier': 200, 'ultimate': 400},
                                'weapon': 'AK gun \x1b[31m︻デ═一 \x1b[0m'},
                    'witcher': {'levels': ['tinkerbell', 'vampire', 'witcher'],
                                'special_attack': 'magic',
                                'max_damage_points': [('tinkerbell', 40), ('vampire', 50), ('witcher', 55)],
                                'max_Current_HP': [('tinkerbell', 50), ('vampire', 70), ('witcher', 80)],
                                'experience_to_next_level': {'vampire': 300, 'witcher': 500},
                                'weapon': 'x gun \x1b[31m╦̵̵̿╤─ ҉ ~\x1b[0m'},
                    'thief': {'levels': ['novice', 'gambit', 'aladin'],
                              'special_attack': 'steal',
                              'max_damage_points': [('novice', 30), ('gambit', 40), ('aladin', 50)],
                              'experience_to_next_level': {'gambit': 390, 'aladin': 550},
                              'max_Current_HP': [('novice', 30), ('gambit', 40), ('aladin', 50)],
                              'weapon': 'sm gun \x1b[31m︻╦╤─\x1b[0m'},
                    'hunter': {'levels': ['Bantu', 'Zulu', 'Masai'],
                               'special_attack': 'knobkerrie',
                               'max_damage_points': [('Bantu', 40), ('Zulu', 60), ('Masai', 80)],
                               'experience_to_next_level': {'Zulu': 400, 'Masai': 600},
                               'max_Current_HP': [('Bantu', 50), ('Zulu', 60), ('Masai', 70)],
                               'weapon': 'sm gun \x1b[31m︻╦̵̵͇̿̿̿̿╤──\x1b[0m'}}

        self.assertEqual(expected, actual)
