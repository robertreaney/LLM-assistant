import wave
import sys
import pyaudio
from pathlib import Path
from typing import Union

from .utils import key_pressed

def record_audio(output:Union[Path,str]='output.wav'):
    output = Path(output)

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1 if sys.platform == 'darwin' else 2
    RATE = 16000
    RECORD_SECONDS = 30 # maximum duration

    # open the audio file
    with wave.open(output.as_posix(), 'wb') as wf:
        p = pyaudio.PyAudio()
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)

        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True)

        print('Recording...press any key to stop!')
        try:
            for _ in range(0, RATE // CHUNK * RECORD_SECONDS):
                wf.writeframes(stream.read(CHUNK))
                if key_pressed():
                    print("Key pressed, exiting loop!")
                    break
        except KeyboardInterrupt:
            pass
        print('Done')

        stream.close()
        p.terminate()


