from game import story_intro_level_one_zaire_area
from unittest import TestCase


class TestStoryIntroLevelOneZaireArea(TestCase):
    maxDiff = None

    def test_intro_level_one_zaire_area_dictionary_unchanged(self):
        mock_character = {'Current level': 'ultimate'}
        story_intro_level_one_zaire_area(mock_character)
        mock_character_after_function_called = {'Current level': 'ultimate'}
        self.assertEqual(mock_character_after_function_called, mock_character)
