import sys
sys.path.insert(0, '../PySubtitle')

from PySubtitle.audio_extraction import extract_audio
from PySubtitle.speech_recognition import audio_to_text
from PySubtitle.vtt_generation import generate_vtt

def main():
    # Chemin vers la vidéo source
    video_path = "./tests/test.mp4"
    
    # Extraire l'audio de la vidéo
    audio_path = extract_audio(video_path)
    print(f"Audio extrait et sauvegardé à : {audio_path}")
    
    # Convertir l'audio en texte
    transcripts, durations = audio_to_text(audio_path)
    print("Transcription terminée.")
    
    # Générer le fichier VTT
    vtt_file = "./example/output.vtt"
    generate_vtt(transcripts, durations, vtt_file)
    print(f"Fichier VTT généré à : {vtt_file}")

if __name__ == "__main__":
    main()