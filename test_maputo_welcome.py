from unittest import TestCase
from game import maputo_welcome
from unittest.mock import patch
import io
from art import text2art
from colorama import Fore, Style, Back


class TestMaputoWelcome(TestCase):
    maxDiff = None

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_maputo_welcome(self, mock_stdout):
        maputo_welcome()
        expected = Fore.BLACK + Back.YELLOW + text2art("Maputo", font='black', chr_ignore=True) + Style.RESET_ALL
        message_printed = mock_stdout.getvalue()
        self.assertTrue(expected in message_printed)


