from game import story_intro_level_zero_maputo_area
from unittest import TestCase
from unittest.mock import patch
import io


class TestIntroLevelMaputo(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)  # if we are getting output
    def test_story_level_maputo(self, mock_stdout):
        story_intro_level_zero_maputo_area()
        game_printed = mock_stdout.getvalue()
        expected = "Once upon a time in the great land of ZAMUNDA, people lived in harmony.\nAll the " \
                   "tribes including the AZIZI, the TIMON, and the PUMBA worked together in peace and " \
                   "harmony.\nThey were hunter gatherers, blacksmiths, rainmakers, farmers - a powerful " \
                   "society.\nAnd they all worshipped KING MUFASA.\nSCAR, MUFASA's brother got jealous and" \
                   "stole RAFIKIS's (the wizard) magic portion to kill MUFASA.\nAfter Mufasa's death, all" \
                   " the tribes turned against each other and peace was no more.\nSCAR killed MUFASA, but" \
                   " not MUFASA's 4 children who managed to escape.\nNow, it is time for revenge.\n" \
                   "MUFASA's children have different powers (classes) and you can choose one to embark on " \
                   "your journey of revenge.\nHere you are at the grasslands of MAPUTO.\n" \
                   "May the gods be with you\n\n"
        self.assertTrue(expected in game_printed)
