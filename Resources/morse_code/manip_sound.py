# https://stackoverflow.com/questions/9770073/sound-generation-synthesis-with-python

import math        #import needed modules
import pyaudio     #sudo apt-get install python-pyaudio
import wave

# https://stackoverflow.com/questions/33513522/when-installing-pyaudio-pip-cannot-find-portaudio-h-in-usr-local-include

PyAudio = pyaudio.PyAudio     #initialize pyaudio

#See https://en.wikipedia.org/wiki/Bit_rate#Audio
FRAME_RATE = 16000     #number of frames per second/frameset.      

FREQUENCY = 500     #Hz, waves per second, 261.63=C4-note.
LENGTH = .2     #seconds to play sound

CHANNELS = 1 # I guess this is for mono sounds

if FREQUENCY > FRAME_RATE:
    FRAME_RATE = FREQUENCY+100

NUMBEROFFRAMES = int(FRAME_RATE * LENGTH)
RESTFRAMES = NUMBEROFFRAMES % FRAME_RATE
WAVEDATA = ''
BLANKDATA = ''

#generating waves
for x in range(NUMBEROFFRAMES):
    WAVEDATA = WAVEDATA+chr(int(math.sin(x/((FRAME_RATE/FREQUENCY)/math.pi))*127+128))    

for x in range(RESTFRAMES): 
    WAVEDATA = WAVEDATA+chr(128)

for x in range(NUMBEROFFRAMES):
    BLANKDATA = WAVEDATA+chr(int(math.sin(x/((FRAME_RATE/10)/math.pi))*127+128))    

for x in range(RESTFRAMES): 
    BLANKDATA = WAVEDATA+chr(128)


sound_frames = []

p = PyAudio()
FORMAT = pyaudio.paInt16
stream = p.open(format = FORMAT, 
                channels = CHANNELS, 
                rate = FRAME_RATE, 
                output = True)

for i in range(4):
    sound_frames.append(BLANKDATA)
    sound_frames.append(WAVEDATA)
    

stream.write(''.join(sound_frames))
stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open('recorded_audio.wav', 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(FRAME_RATE)
wf.writeframes(bytes(sound_frames))
wf.close()