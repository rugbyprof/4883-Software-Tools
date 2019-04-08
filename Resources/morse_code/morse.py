#!/usr/local/bin/python3
# Python program to implement Morse Code Translator 
# https://www.geeksforgeeks.org/morse-code-translator-python/
''' 
short mark, dot or "dit" (▄): "dot duration" is one time unit long
longer mark, dash or "dah" (▄ ▄ ▄): three time units long
inter-element gap between the dots and dashes within a character: one dot duration or one unit long
short gap (between letters): three time units long
medium gap (between words): seven time units long
'''

from pydub import AudioSegment
from pydub.playback import play
import sys
import os
from time import sleep
import numpy as np
import matplotlib.pyplot as plt

os.chdir("/Users/griffin/Code/Courses/1-Current_Courses/4883-Software-Tools/Resources/morse_code")

# Dictionary representing the morse code chart 
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
					'C':'-.-.', 'D':'-..', 'E':'.', 
					'F':'..-.', 'G':'--.', 'H':'....', 
					'I':'..', 'J':'.---', 'K':'-.-', 
					'L':'.-..', 'M':'--', 'N':'-.', 
					'O':'---', 'P':'.--.', 'Q':'--.-', 
					'R':'.-.', 'S':'...', 'T':'-', 
					'U':'..-', 'V':'...-', 'W':'.--', 
					'X':'-..-', 'Y':'-.--', 'Z':'--..', 

					'1':'.----', '2':'..---', '3':'...--', 
					'4':'....-', '5':'.....', '6':'-....', 
					'7':'--...', '8':'---..', '9':'----.', 
					'0':'-----', ', ':'--..--', '.':'.-.-.-', 
					'?':'..--..', '/':'-..-.', '-':'-....-', 
					'(':'-.--.', ')':'-.--.-'} 

# Function to encrypt the string 
# according to the morse code chart 
def to_morse(message): 
	cipher = []
	for letter in message: 
		if letter != ' ': 

			# Looks up the dictionary and adds the 
			# correspponding morse code 
			# along with a space to separate 
			# morse codes for different characters 
			cipher.append(MORSE_CODE_DICT[letter])
		else: 
			# 1 space indicates different characters 
			# and 2 indicates different words 
			cipher.append(' ')

	return cipher 

# Function to decrypt the string 
# from morse to english 
def from_morse(message): 

	# extra space added at the end to access the 
	# last morse code 
	message += ' '

	decipher = '' 
	citext = '' 
	for letter in message: 

		# checks for space 
		if (letter != ' '): 

			# counter to keep track of space 
			i = 0

			# storing morse code of a single character 
			citext += letter 

		# in case of space 
		else: 
			# if i = 1 that indicates a new character 
			i += 1

			# if i = 2 that indicates a new word 
			if i == 2 : 

				# adding space to separate words 
				decipher += ' '
			else: 

				# accessing the keys using their values (reverse of encryption) 
				decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT 
				.values()).index(citext)] 
				citext = '' 

	return decipher


def sound_to_morse(sound_file):

	song_data = sound_file_info(sound_file)

	zero = 0
	not_zero = 0

	ditdot = []

	for i in range(0,len(song_data['raw_data']),100):
		# if i == 0:
		# 	zero += 1
		# else:
		#     not_zero += 1
		s = sum(song_data['raw_data'][i:i+100])
		ditdot.append(s)
	

	blanks = 0
	for d in ditdot:
		if d == 0:
			blanks += 1
		else:
			break
	
	ditdot = ditdot[blanks:]
	letters = []

	i = -1
	p = None
	for d in ditdot:
		if (d > 0) != p:
			letters.append(0)
			i += 1
			if d > 0:
				p = True
			else:
				p = False
		letters[i] += 1

	print(letters)
		
		


def sound_file_info(sound_file):
	print(os.path.basename(sound_file))
	name,ext = os.path.basename(sound_file).split('.')

	file_data = AudioSegment.from_file(sound_file, ext)

	data = {}
	# get raw audio data as a bytestring
	data['raw_data'] = file_data.raw_data
	# get the frame rate
	data['sample_rate'] = file_data.frame_rate
	# get amount of bytes contained in one sample
	data['sample_size'] = file_data.sample_width
	# get channels
	data['channels'] = file_data.channels

	return data

def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'valid') / w

def show_sound_data(raw_data):

	raw_nums = np.frombuffer(raw_data, dtype=np.int16)
	time = [x for x in range(len(raw_nums))]

	plt.plot(time, raw_nums, color='orange')
	plt.xlabel('Time')
	plt.ylabel('Sound')
	plt.title('Morse Sound File')
	plt.show()

	#############################################

	raw_nums = moving_average(raw_nums,103)

	digital_signal = []

	for d in raw_nums:
		if d == 0.0:
			digital_signal.append(0)
		else:
			digital_signal.append(1)

	time = [x for x in range(len(raw_nums))]

	plt.plot(time, digital_signal, color='red')
	plt.xlabel('Time')
	plt.ylabel('Sound')
	plt.title('Morse Sound File')
	#plt.show()

	#############################################

	raw_nums = moving_average(digital_signal,5)

	digital_signal = []

	for d in raw_nums:
		if d == 0.0:
			digital_signal.append(0)
		else:
			digital_signal.append(1)

	time = [x for x in range(len(digital_signal))]

	plt.plot(time, digital_signal, color='blue', alpha=0.5)
	plt.xlabel('Time')
	plt.ylabel('Sound')
	plt.title('Morse Sound File')
	plt.show()

	f = open("raw.dat","w")
	for d in digital_signal:
		if d == 0.0:
			f.write("0")
		else:
			f.write("1")
	f.close()


def msound(beep,milli_length=500):
	millis = len(beep)
	start = 0
	end = milli_length
	return beep[start:end]

# Hard-coded driver function to run the program 
def main(): 
	message = "coded message."
	code = to_morse(message.upper()) 
	print (code) 


	dot = AudioSegment.from_ogg("./sound_files/dot.ogg")
	dash = AudioSegment.from_ogg("./sound_files/dash.ogg")
	blank = AudioSegment.from_ogg("./sound_files/blank.ogg")

	result = blank

	for letter in code:
		result += blank[:300]
		for c in letter:
			if '-' in c:
				result += dash
				result += blank[:100]
			elif '.' in c:
				result += dot
				result += blank[:100]
			else:
				result += blank

	#play(result)
	result.export("./sound_files/result.mp3", format="ogg")


# Executes the main function 
if __name__ == '__main__': 
	#main() 
	data = sound_file_info('./sound_files/result.mp3')
	show_sound_data(data['raw_data'])
	#sound_to_morse('./sound_files/result.mp3')