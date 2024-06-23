# PySubtitle/speech_recognition.py

import tempfile
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence
import speech_recognition as sr

def audio_to_text(audio_path):
    recognizer = sr.Recognizer()
    sound = AudioSegment.from_wav(audio_path)
    chunks = split_on_silence(sound,
                              min_silence_len=500,
                              silence_thresh=sound.dBFS-14,
                              keep_silence=250)

    full_text = []
    durations = []

    # Création d'un répertoire temporaire pour stocker les fichiers audio découpés
    with tempfile.TemporaryDirectory() as temp_dir:
        for i, chunk in enumerate(chunks):
            chunk_silent = AudioSegment.silent(duration=100)
            audio_chunk = chunk + chunk_silent
            chunk_filename = os.path.join(temp_dir, f"chunk{i}.wav")
            audio_chunk.export(chunk_filename, format="wav")
            durations.append(len(audio_chunk) / 1000.0)

            with sr.AudioFile(chunk_filename) as source:
                audio = recognizer.record(source)
                try:
                    text = recognizer.recognize_google(audio)
                    full_text.append(text)
                except sr.UnknownValueError:
                    full_text.append("")
                except sr.RequestError as e:
                    full_text.append(f"Error: {e}")

    return full_text, durations
