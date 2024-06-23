import sys
sys.path.insert(0, '../PySubtitle')
import unittest
from PySubtitle.speech_recognition import audio_to_text

TRANSCRIPTION_EXPECTED = "today we're going to be practicing your speaking and conversational skills by having a conversation you and me"

class TestSpeechRecognition(unittest.TestCase):
    def test_audio_to_text(self):
        # Utilisez un petit fichier audio de test avec un contenu connu
        audio_path = "tests/chunk0.wav"
        transcripts, durations = audio_to_text(audio_path)
        print(transcripts)
        print(durations)
        # Vérifiez si la transcription est correcte
        self.assertEqual(" ".join(transcripts), TRANSCRIPTION_EXPECTED)
        # Vérifiez si la durée est raisonnablement calculée
        self.assertTrue(all(duration > 0 for duration in durations))

if __name__ == '__main__':
    unittest.main()