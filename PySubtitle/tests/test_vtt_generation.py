# tests/test_vtt_generation.py

import unittest
from PySubtitle.vtt_generation import generate_vtt
import os

class TestVTTGeneration(unittest.TestCase):
    def test_generate_vtt(self):
        transcripts = ["Ceci est un test.", "Ceci est un second test."]
        durations = [2.5, 3.0]
        vtt_file = "tests/output.vtt"
        generate_vtt(transcripts, durations, vtt_file)
        # Vérifiez si le fichier VTT est créé
        self.assertTrue(os.path.exists(vtt_file))
        # Nettoyez après le test
        os.remove(vtt_file)

if __name__ == '__main__':
    unittest.main()