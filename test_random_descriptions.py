from game import random_descriptions
from unittest import TestCase
from unittest.mock import patch
from colorama import Fore, Style


class TestRandomDescriptions(TestCase):
    @patch('random.randint', return_value=0)  # random number
    def test_random_descriptions_first_description_maputo_area(self, _):
        mock_character = {'Current location': 'Maputo'}
        result = random_descriptions(mock_character)
        expected = ("MAPUTO is a land of beauty. And this scenery is an example. Sometimes you scratch your head"
                    "because you don't know where to go.\n(⊙.☉)7\nA Hornbill bird flies by,  enjoying the sun."
                    "You could kill it but Hornbills are a sign of good luck.\nYou keep moving\n"
                    "___________________________________________________________________\n")
        self.assertEqual(expected, result)

    @patch('random.randint', return_value=0)  # random number
    def test_random_descriptions_first_description_zaire_area(self, _):
        mock_character = {'Current location': 'Zaire'}
        result = random_descriptions(mock_character)
        expected = ("You see a sign. It says 'MUFASA_TRIBE'.\n" + Fore.RED + "➶➶➶➶➶ƭεรƭ➷➷➷➷➷" + Style.RESET_ALL +
                    "This gives you shivers. But you are brave.\nbThe sun is setting. Maybe you need some rest?\n"
                    "___________________________________________________________________\n")
        self.assertEqual(expected, result)

    @patch('random.randint', return_value=4)  # random number
    def test_random_descriptions_last_description_zaire_area(self, _):
        mock_character = {'Current location': 'Zaire'}
        result = random_descriptions(mock_character)
        expected = ("ᕦ(ò_óˇ)ᕤ\nSomeone who needs to fight scar must exercise. You do so here and feel rejuvenated.\n"
                    "Well done!\n ___________________________________________________________________\n")
        self.assertEqual(expected, result)

    @patch('random.randint', return_value=5)  # random number
    def test_random_descriptions_last_description_maputo_area(self, _):
        mock_character = {'Current location': 'Maputo'}
        result = random_descriptions(mock_character)
        expected = ("This seems like a quiet place. You sit down to write some ideas.\nPerhaps its about how you will "
                    "defeat SCAR?\n" + Fore.LIGHTRED_EX + "((̲̅ ̲̅(̲̅C̲̅r̲̅a̲̅y̲̅o̲̅l̲̲̅̅a̲̅( ̲̅((> "
                    + Style.RESET_ALL +
                    "\nFailing to plan is planning to "
                    "fail\n___________________________________________________________________\n")
        self.assertEqual(expected, result)

    @patch('random.randint', return_value=5)  # random number
    def test_random_descriptions_dictionary_character_not_changed(self, _):
        mock_character = {'Current location': 'Maputo',
                          'Current level': 'Zulu',
                          'Current_damage_points': 50}
        random_descriptions(mock_character)
        mock_character_after_function_invoked = {'Current location': 'Maputo',
                                                 'Current level': 'Zulu',
                                                 'Current_damage_points': 50}

        self.assertEqual(mock_character, mock_character_after_function_invoked)
