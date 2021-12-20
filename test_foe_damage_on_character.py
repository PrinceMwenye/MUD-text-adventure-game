from game import foe_damage_on_character
from unittest import TestCase
from unittest.mock import patch
import io


class TestFoeDamageOnCharacter(TestCase):
    @patch('random.randint', return_value=20)  # random number
    @patch('random.choices', return_value=[True])  # random number
    @patch('sys.stdout', new_callable=io.StringIO)  # if we are getting output
    def test_character_foe_damage_on_character_level_zero(self, _, __, ___):  # Zaire
        character = {'class_attributes': {'levels': ['novice', 'soldier', 'ultimate']},
                     'Current level': 'novice', 'Current HP': 40}  # novice is at index zero in class attributes
        foe_damage_on_character(character)
        expected_character_current_hp = 20
        self.assertEqual(expected_character_current_hp, character['Current HP'])

    @patch('random.randint', return_value=30)  # random number
    @patch('random.choices', return_value=[True])  # random number
    @patch('sys.stdout', new_callable=io.StringIO)  # if we are getting output
    def test_character_foe_damage_on_character_level_one(self, _, __, ___):  # Maputo
        character = {'class_attributes': {'levels': ['novice', 'soldier', 'ultimate']},
                     'Current level': 'soldier', 'Current HP': 55}  # soldier is at index one in class attributes
        foe_damage_on_character(character)
        expected_character_current_hp = 25
        self.assertEqual(expected_character_current_hp, character['Current HP'])

    @patch('random.randint', return_value=30)  # random number
    @patch('random.choices', return_value=[False])  # random number
    @patch('sys.stdout', new_callable=io.StringIO)  # if we are getting output
    def test_character_foe_damage_on_character_no_damage_level_one_dictionary_not_changed(self, _, __, ___):  # Maputo
        initial_character = {'class_attributes': {'levels': ['novice', 'soldier', 'ultimate']},
                             'Current level': 'soldier',
                             'Current HP': 55}  # soldier is at index one in class attributes
        character_after_function_invoked = {'class_attributes': {'levels': ['novice', 'soldier', 'ultimate']},
                                            'Current level': 'soldier',
                                            'Current HP': 55}  # soldier is at index one in class attributes

        foe_damage_on_character(initial_character)
        self.assertEqual(initial_character, character_after_function_invoked)
