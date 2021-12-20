from game import check_boss_dying
from unittest import TestCase
from unittest.mock import patch
import io


class TestCheckBossDying(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)  # if we are getting output
    def test_check_boss_dying_true(self, mock_stdout):
        boss_health = 100
        check_boss_dying(boss_health)
        game_printed_this = mock_stdout.getvalue()
        expected = "\u001b[34;1mBoss shows minor damage, you have to fight harder\u001b[0m\n" \
                   f"\u001b[34;1mBoss health is at {boss_health}\u001b[0m\n"
        self.assertEqual(expected, game_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)  # if we are getting output
    def test_check_boss_dying_false(self, mock_stdout):
        boss_health = 10
        check_boss_dying(boss_health)
        game_printed_this = mock_stdout.getvalue()
        expected = "\u001b[31;1mBoss bleeds heavily.\n You are on the verge of victory\u001b[0m\n" \
                   f"\u001b[31;1mBoss health is at {boss_health}\u001b[0m\nThe tribes sing:\n" \
                   f"SCAR IS DYING\n" \
                   f"SCAR IS DYING\n"\
                   f"SCAR IS DYING\n"\

        self.assertEqual(expected, game_printed_this)


        



