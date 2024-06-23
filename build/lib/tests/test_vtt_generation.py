# tests/test_vtt_generation.py
import sys
sys.path.insert(0, '../PySubtitle')
import unittest
from PySubtitle.vtt_generation import generate_vtt
import os

class TestVTTGeneration(unittest.TestCase):
    def test_generate_vtt(self):
        transcripts = ['today', "we're going to be practicing your speaking and conversational skills by having a conversation you and me"]
        durations = [1.175, 8.101]
        vtt_file = "tests/output.vtt"
        generate_vtt(transcripts, durations, vtt_file)
        # Vérifiez si le fichier VTT est créé
        self.assertTrue(os.path.exists(vtt_file))
        # Nettoyez après le test
        os.remove(vtt_file)

if __name__ == '__main__':
    unittest.main()