from pyguide.audio_io import record_audio
from pyguide.asr import speech_to_text

def speak_input(file):
    record_audio(file)
    translation = speech_to_text(file)
    print(translation[0]['transcription'])