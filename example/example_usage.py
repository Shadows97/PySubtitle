import sys
import os

sys.path.insert(0, '../PySubtitle')

from PySubtitle.audio_extraction import extract_audio
from PySubtitle.speech_recognition import audio_to_text
from PySubtitle.vtt_generation import generate_vtt
from PySubtitle.languages import Languages


def main():
    # Get the directory yof the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Path to the video source
    video_dir = os.path.join(script_dir, '..', 'tests')
    video_file = 'test.mp4'
    video_path = os.path.join(video_dir, video_file)

    # Check if the file exists
    if not os.path.isfile(video_path):
        print(f"Error: The file {video_path} does not exist.")
        return

    # Extract audio from the video
    audio_path = extract_audio(video_path)
    print(f"Audio extracted and saved at: {audio_path}")

    # Convert audio to text
    transcripts, durations = audio_to_text(audio_path, source_language=Languages.ENGLISH.value)
    print("Transcription completed.")

    # Generate the VTT file
    vtt_file = os.path.join(script_dir, 'output.vtt')
    generate_vtt(transcripts, durations, vtt_file)
    print(f"VTT file generated at: {vtt_file}")


if __name__ == "__main__":
    main()
