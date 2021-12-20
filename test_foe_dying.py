from game import check_foe_dying
from unittest import TestCase
from unittest.mock import patch
import io


class TestCheckFoeDying(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)  # if we are getting output
    def test_foe_dying_yes(self, mock_stdout):
        foe_health = 30
        check_foe_dying(foe_health)
        game_printed_this = mock_stdout.getvalue()
        expected = "Foe bleeds heavily, you are on the verge of victory"
        self.assertTrue(expected in game_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)  # if we are getting output
    def test_foe_dying_not_yet(self, mock_stdout):
        foe_health = 31
        check_foe_dying(foe_health)
        game_printed_this = mock_stdout.getvalue()
        expected = "Foe has minor scratches, you have to fight harder!"
        self.assertTrue(expected in game_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)  # if we are getting output
    def test_foe_dying_foe_healthy(self, mock_stdout):
        foe_health = 100
        check_foe_dying(foe_health)
        game_printed_this = mock_stdout.getvalue()
        expected = "Foe has minor scratches, you have to fight harder!"
        self.assertTrue(expected in game_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)  # if we are getting output
    def test_foe_dying_foe_at_zero(self, mock_stdout):
        foe_health = 0
        check_foe_dying(foe_health)
        game_printed_this = mock_stdout.getvalue()
        expected = "Foe bleeds heavily, you are on the verge of victory"
        self.assertTrue(expected in game_printed_this)


