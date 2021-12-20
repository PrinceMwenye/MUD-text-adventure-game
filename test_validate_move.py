from unittest import TestCase
from game import validate_move


class TestValidateMove(TestCase):
    def test_validate_move_east_at_boundary(self):
        character = {'X-coordinate': 25, 'Y-coordinate': 0, 'Current HP': 5}
        direction = "East"
        rows = 25
        columns = 25
        expected = False
        actual = validate_move(direction, character, rows, columns)
        self.assertEqual(expected, actual)

    def test_validate_move_north_at_boundary(self):
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        direction = "North"
        rows = 25
        columns = 25
        expected = False
        actual = validate_move(direction, character, rows, columns)
        self.assertEqual(expected, actual)

    def test_validate_move_south_at_boundary(self):
        character = {'X-coordinate': 0, 'Y-coordinate': 25, 'Current HP': 5}
        direction = "South"
        expected = False
        rows = 25
        columns = 25
        actual = validate_move(direction, character, rows, columns)
        self.assertEqual(expected, actual)

    def test_validate_move_west_at_boundary(self):
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        direction = "West"
        expected = False
        rows = 25
        columns = 25
        actual = validate_move(direction, character, rows, columns)
        self.assertEqual(expected, actual)

    def test_validate_move_east_from_start_point(self):
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        direction = "East"
        expected = True
        rows = 25
        columns = 25
        actual = validate_move(direction, character, rows, columns)
        self.assertEqual(expected, actual)

    def test_validate_move_south_from_start_point(self):
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        direction = "South"
        expected = True
        rows = 25
        columns = 25
        actual = validate_move(direction, character, rows, columns)
        self.assertEqual(expected, actual)

    def test_validate_move_south_from_middle(self):
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        direction = "South"
        expected = True
        rows = 25
        columns = 25
        actual = validate_move(direction, character, rows, columns)
        self.assertEqual(expected, actual)

    def test_validate_move_north_from_middle(self):
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        direction = "North"
        expected = True
        rows = 25
        columns = 25
        actual = validate_move(direction, character, rows, columns)

        self.assertEqual(expected, actual)

    def test_validate_move_dictionary_character_not_changed(self):
        original_character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        original_character_copy = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        direction = "North"
        rows = 25
        columns = 25
        validate_move(direction, original_character, rows, columns)
        self.assertEqual(original_character, original_character_copy)
