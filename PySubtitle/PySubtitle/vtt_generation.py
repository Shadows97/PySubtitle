# nom_de_votre_bibliotheque/vtt_generation.py

from webvtt import WebVTT, Caption

def generate_vtt(transcripts, durations, vtt_file):
    vtt = WebVTT()
    start_time = 0
    for transcript, duration in zip(transcripts, durations):
        if transcript:  # Only add non-empty transcripts
            end_time = start_time + duration
            caption = Caption(
                f"{int(start_time//3600):02}:{int((start_time%3600)//60):02}:{int(start_time%60):02}.000",
                f"{int(end_time//3600):02}:{int((end_time%3600)//60):02}:{int(end_time%60):02}.000",
                transcript
            )
            vtt.captions.append(caption)
            start_time = end_time

    vtt.save(vtt_file)