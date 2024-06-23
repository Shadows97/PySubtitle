import sys
sys.path.insert(0, '../PySubtitle')

import unittest
from PySubtitle.audio_extraction import extract_audio
import os

class TestAudioExtraction(unittest.TestCase):
    def test_extract_audio(self):
        # Supposons que vous avez un fichier vidéo de test dans le dossier de test
        video_path = "tests/test.mp4"
        audio_path = extract_audio(video_path)
        # Vérifiez si le fichier audio est créé
        self.assertTrue(os.path.exists(audio_path))
        # Nettoyez après le test
        os.remove(audio_path)

if __name__ == '__main__':
    unittest.main()