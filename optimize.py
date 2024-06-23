import ffmpeg
from pydub import AudioSegment
from pydub.silence import split_on_silence
import speech_recognition as sr
from webvtt import WebVTT, Caption

def extract_audio(video_path, audio_format="wav"):
    output = video_path.replace(".mp4", f".{audio_format}")
    ffmpeg.input(video_path).output(output, acodec='pcm_s16le', ac=1, ar='16k').run()
    return output

def audio_to_text(audio_path, language="fr-FR"):
    recognizer = sr.Recognizer()
    sound = AudioSegment.from_wav(audio_path)
    chunks = split_on_silence(sound,
                              min_silence_len=500,
                              silence_thresh=sound.dBFS-14,
                              keep_silence=250)  # Réduit la durée de silence conservée

    full_text = []
    durations = []  # Liste pour stocker la durée de chaque segment
    for i, chunk in enumerate(chunks):
        chunk_silent = AudioSegment.silent(duration=10)  # Ajoute un peu de silence à la fin
        audio_chunk = chunk + chunk_silent
        audio_chunk.export(f"./media/audio/chunk{i}.wav", format="wav")
        durations.append(len(audio_chunk) / 1000.0)  # Calcule la durée en secondes

        with sr.AudioFile(f"./media/audio/chunk{i}.wav") as source:
            audio = recognizer.record(source)
            try:
                text = recognizer.recognize_google(audio)
                full_text.append(text)
            except sr.UnknownValueError:
                full_text.append("")
            except sr.RequestError as e:
                full_text.append(f"Error: {e}")

    return full_text, durations

def generate_vtt(transcripts, durations, vtt_file):
    vtt = WebVTT()
    start_time = 0
    for transcript, duration in zip(transcripts, durations):
        if transcript:  # Ajoute uniquement les transcriptions non vides
            end_time = start_time + duration
            caption = Caption(
                f"{int(start_time//3600):02}:{int((start_time%3600)//60):02}:{int(start_time%60):02}.000",
                f"{int(end_time//3600):02}:{int((end_time%3600)//60):02}:{int(end_time%60):02}.000",
                transcript
            )
            vtt.captions.append(caption)
            start_time = end_time  # Met à jour le start_time pour le prochain sous-titre

    vtt.save(vtt_file)

def main(video_path):
    audio_path = extract_audio(video_path)
    transcripts, durations = audio_to_text(audio_path)
    generate_vtt(transcripts, durations, "output.vtt")

if __name__ == "__main__":
    main("media/videos/test.mp4")

