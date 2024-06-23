# PySubtitle

PySubtitle is a Python library designed to automate the process of generating subtitles for video files. It extracts audio from video files, converts the audio to text using Google's speech recognition services, and generates VTT (Web Video Text Tracks) files for subtitles. This library is particularly useful for creating subtitles for videos in various languages, making content more accessible to a wider audience.

## Features

- **Audio Extraction**: Extracts audio from video files using `ffmpeg`.
- **Speech Recognition**: Converts audio to text using Google Cloud Speech-to-Text API.
- **Subtitle Generation**: Creates VTT files from the transcribed text, with accurate timing and synchronization.
- **Cross-Platform**: Works on Windows, macOS, and Linux.

## Prerequisites

Before installing and using this library, you need to ensure the following prerequisites are met:

1. **FFmpeg**: This library requires `ffmpeg` to handle video and audio processing. Here's how you can install `ffmpeg`:

   ### On Ubuntu:
   ```bash
   sudo apt update
   sudo apt install ffmpeg
   ```

   ### On macOS:
   ```bash
   brew install ffmpeg
   ```

   ### On Windows:
   Download the binaries from [FFmpeg Official Site](https://ffmpeg.org/download.html) and follow the installation instructions.

2. **Google Cloud Service Key**: This library uses Google Cloud Speech-to-Text API for speech recognition. You need to set up a Google Cloud project and download a service key. Follow these steps:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project or select an existing one.
   - Enable the Speech-to-Text API for your project.
   - Go to "Credentials" and create a new service account key.
   - Download the JSON key file and set the environment variable `GOOGLE_APPLICATION_CREDENTIALS` to the path of the JSON file.

## Installation

To install this library, use pip:

```bash
pip install PySubtitle
```

## Usage

Here is a simple example of how to use this library:

```python
from PySubtitle.audio_extraction import extract_audio
from PySubtitle.speech_recognition import audio_to_text
from PySubtitle.vtt_generation import generate_vtt

# Path to your video file
video_path = 'path/to/your/video.mp4'

# Extract audio
audio_path = extract_audio(video_path)

# Convert audio to text
transcripts, durations = audio_to_text(audio_path)

# Generate VTT file
vtt_file = 'output.vtt'
generate_vtt(transcripts, durations, vtt_file)
```

## Contributing

Contributions are always welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
