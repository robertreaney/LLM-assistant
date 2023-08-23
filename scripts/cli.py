import argparse
from pyguide.audio_io import record_audio, playback

def main():
    parser = argparse.ArgumentParser(description="A simple CLI for PyGuide Language Assistant.")
    subparsers = parser.add_subparsers(dest='subcommand')

    # audio recording
    record_parser = subparsers.add_parser('record', help='Record something')
    record_parser.add_argument('-f', '--file', help='File to save recording', default='output.wav')
    
    playback_parser = subparsers.add_parser('play', help='Play a recording')
    playback_parser.add_argument('-f', '--file', help='File to playback from', default='output.wav')
    
    args = parser.parse_args()

    if args.subcommand == 'record':
        record_audio(args.file)
    elif args.subcommand == 'play':
        playback(args.file)

if __name__ == "__main__":
    main()
