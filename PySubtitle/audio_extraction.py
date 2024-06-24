import ffmpeg
import os
from concurrent.futures import ThreadPoolExecutor

def extract_audio(video_path, audio_format="wav"):
    output = video_path.replace(".mp4", f".{audio_format}")
    ffmpeg.input(video_path).output(output, acodec='pcm_s16le', ac=1, ar='16k').run(overwrite_output=True)
    return output

def extract_audio_parallel(video_paths, audio_format="wav"):
    def _extract_single_video(video_path):
        return extract_audio(video_path, audio_format)

    with ThreadPoolExecutor() as executor:
        audio_files = list(executor.map(_extract_single_video, video_paths))

    return audio_files