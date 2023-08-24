import argparse
from pyguide.audio_io import record_audio, playback
from pyguide import speak_input
from pyguide.asr import speech_to_text

def main():
    parser = argparse.ArgumentParser(description="A simple CLI for PyGuide Language Assistant.")
    subparsers = parser.add_subparsers(dest='subcommand')

    # audio recording
    record_parser = subparsers.add_parser('record', help='Record something')
    record_parser.add_argument('-f', '--file', help='File to save recording', default='output.wav')
    
    playback_parser = subparsers.add_parser('play', help='Play a recording')
    playback_parser.add_argument('-f', '--file', help='File to playback from', default='output.wav')

    playback_parser = subparsers.add_parser('translate', help='Automatic Speech Recognition (ASR)')
    playback_parser.add_argument('-f', '--file', help='File to playback from', default='output.wav')

    playback_parser = subparsers.add_parser('asr', help='Run interactive ASR')
    playback_parser.add_argument('-f', '--file', help='File to playback from', default='output.wav')
    
    args = parser.parse_args()

    if args.subcommand == 'record':
        record_audio(args.file)
    elif args.subcommand == 'play':
        playback(args.file)
    elif args.subcommand == 'translate':
        print(speech_to_text(args.file)[0]['transcription'])
    elif args.subcommand == 'asr':
        speak_input(args.file)

if __name__ == "__main__":
    main()
