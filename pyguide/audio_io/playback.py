import wave
import sys
from pathlib import Path
from typing import Union
import pyaudio

from .utils import key_pressed

def playback(input:Union[Path,str]='output.wav'):
    input = Path(input).as_posix()
    CHUNK = 1024

    with wave.open(input, 'rb') as wf:
        # Instantiate PyAudio and initialize PortAudio system resources (1)
        p = pyaudio.PyAudio()

        # Open stream (2)
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        # Play samples from the wave file (3)
        print('Playing back audio...press any key to stop!')
        try:
            while len(data := wf.readframes(CHUNK)):  # Requires Python 3.8+ for :=
                stream.write(data)
                if key_pressed():
                    print("Key pressed, exiting loop!")
                    break
        except KeyboardInterrupt:
            pass

        # Close stream (4)
        stream.close()

        # Release PortAudio system resources (5)
        p.terminate()