from game import make_character
from unittest import TestCase
from unittest.mock import patch
import io


class TestMakeCharacter(TestCase):
    @patch('builtins.input', side_effect=['Prince', '1'])  # user input
    @patch('sys.stdout', new_callable=io.StringIO)  # if we are getting output
    def test_make_character_fighter_class(self, _, __):
        mock_character = make_character()
        expected = {'xp': 0,
                    'name': 'PRINCE',
                    'class': 'fighter',
                    'class_attributes': {'levels': ['novice', 'soldier', 'ultimate'],
                                         'special_attack': 'sword',
                                         'max_damage_points': [('novice', 20), ('soldier', 30), ('ultimate', 40)],
                                         'max_Current_HP': [('novice', 50), ('soldier', 70), ('ultimate', 80)],
                                         'experience_to_next_level': {'soldier': 200, 'ultimate': 400},
                                         'weapon': 'AK gun \x1b[31m︻デ═一 \x1b[0m'},
                    'Current level': 'novice',
                    'Current location': 'Maputo',
                    'Current HP': 50,
                    'X-coordinate': 0,
                    'Y-coordinate': 0,
                    'location levels': ['Maputo', 'Zaire', 'Zamunda'],
                    'Current_damage_points': 20,
                    'weapon': 'AK gun \x1b[31m︻デ═一 \x1b[0m'}
        self.assertEqual(expected, mock_character)

    @patch('builtins.input', side_effect=['Prince', '2'])  # user input
    @patch('sys.stdout', new_callable=io.StringIO)  # if we are getting output
    def test_make_character_witcher_class(self, _, __):
        mock_character = make_character()
        expected = {'xp': 0,
                    'name': 'PRINCE',
                    'class': 'witcher',
                    'class_attributes': {'levels': ['tinkerbell', 'vampire', 'witcher'],
                                         'special_attack': 'magic',
                                         'max_damage_points': [('tinkerbell', 40), ('vampire', 50), ('witcher', 55)],
                                         'max_Current_HP': [('tinkerbell', 50), ('vampire', 70), ('witcher', 80)],
                                         'experience_to_next_level': {'vampire': 300, 'witcher': 500},
                                         'weapon': 'x gun\x1b[31m╦̵̵̿╤─ ҉ ~\x1b[0m'},
                    'Current level': 'tinkerbell',
                    'Current location': 'Maputo',
                    'Current HP': 50,
                    'X-coordinate': 0,
                    'Y-coordinate': 0,
                    'location levels': ['Maputo', 'Zaire', 'Zamunda'],
                    'Current_damage_points': 40,
                    'weapon': 'x gun\x1b[31m╦̵̵̿╤─ ҉ ~\x1b[0m'}

        self.assertEqual(expected, mock_character)

    @patch('builtins.input', side_effect=['Prince', '3'])  # user input
    @patch('sys.stdout', new_callable=io.StringIO)  # if we are getting output
    def test_make_character_thief_class(self, _, __):
        mock_character = make_character()
        expected = {'xp': 0,
                    'name': 'PRINCE',
                    'class': 'thief',
                    'class_attributes': {'levels': ['novice', 'gambit', 'aladin'],
                                         'special_attack': 'steal',
                                         'max_damage_points': [('novice', 30), ('gambit', 40), ('aladin', 50)],
                                         'experience_to_next_level': {'gambit': 390, 'aladin': 550},
                                         'max_Current_HP': [('novice', 30), ('gambit', 40), ('aladin', 50)],
                                         'weapon': 'sm gun\x1b[31m︻╦╤─\x1b[0m'},
                    'Current level': 'novice',
                    'Current location': 'Maputo',
                    'Current HP': 30,
                    'X-coordinate': 0,
                    'Y-coordinate': 0,
                    'location levels': ['Maputo', 'Zaire', 'Zamunda'],
                    'Current_damage_points': 30,
                    'weapon': 'sm gun\x1b[31m︻╦╤─\x1b[0m'}

        self.assertEqual(expected, mock_character)

    @patch('builtins.input', side_effect=['Prince', '4'])  # user input
    @patch('sys.stdout', new_callable=io.StringIO)  # if we are getting output
    def test_make_character_hunter_class(self, _, __):
        mock_character = make_character()
        expected = {'xp': 0,
                    'name': 'PRINCE',
                    'class': 'hunter',
                    'class_attributes': {'levels': ['Bantu', 'Zulu', 'Masai'],
                                         'special_attack': 'knobkerrie',
                                         'max_damage_points': [('Bantu', 40), ('Zulu', 60), ('Masai', 80)],
                                         'experience_to_next_level': {'Zulu': 400, 'Masai': 600},
                                         'max_Current_HP': [('Bantu', 50), ('Zulu', 60), ('Masai', 70)],
                                         'weapon': 'sm gun\x1b[31m︻╦̵̵͇̿̿̿̿╤──\x1b[0m'},
                    'Current level': 'Bantu',
                    'Current location': 'Maputo',
                    'Current HP': 50,
                    'X-coordinate': 0,
                    'Y-coordinate': 0,
                    'location levels': ['Maputo', 'Zaire', 'Zamunda'],
                    'Current_damage_points': 40,
                    'weapon': 'sm gun\x1b[31m︻╦̵̵͇̿̿̿̿╤──\x1b[0m'}

        self.assertEqual(expected, mock_character)
