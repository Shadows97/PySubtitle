# tests/test_speech_recognition.py

import unittest
from PySubtitle.speech_recognition import audio_to_text

class TestSpeechRecognition(unittest.TestCase):
    def test_audio_to_text(self):
        # Utilisez un petit fichier audio de test avec un contenu connu
        audio_path = "tests/test_audio.wav"
        transcripts, durations = audio_to_text(audio_path)
        # Vérifiez si la transcription est correcte
        self.assertIn("exemple de transcription", transcripts)
        # Vérifiez si la durée est raisonnablement calculée
        self.assertTrue(all(duration > 0 for duration in durations))

if __name__ == '__main__':
    unittest.main()