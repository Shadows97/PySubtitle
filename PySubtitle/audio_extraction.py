# nom_de_votre_bibliotheque/audio_extraction.py

import ffmpeg

def extract_audio(video_path, audio_format="wav"):
    output = video_path.replace(".mp4", f".{audio_format}")
    ffmpeg.input(video_path).output(output, acodec='pcm_s16le', ac=1, ar='16k').run()
    return output