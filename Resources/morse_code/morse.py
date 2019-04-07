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
def encrypt(message): 
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
def decrypt(message): 

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

def msound(beep,milli_length=500):
	millis = len(beep)
	start = 0
	end = milli_length
	return beep[start:end]

# Hard-coded driver function to run the program 
def main(): 
	message = "This is a morse code message."
	code = encrypt(message.upper()) 
	print (code) 

	beep = AudioSegment.from_mp3("./sound_files/beep-09.mp3")

	dot = AudioSegment.from_ogg("./sound_files/dot.ogg")
	dash = AudioSegment.from_ogg("./sound_files/dash.ogg")

	raw_dot = dot.raw_data
	raw_dash = dash.raw_data

	print(len(dot))
	print(len(dash))

	sys.exit()


	# dot = msound(beep,150)
	# dash = msound(beep,500)

	result = beep[:10]

	for letter in code:
		for c in letter:
			if '-' in c:
				result += dash
			elif '.' in c:
				result += dot
			else:
				#sleep(.3)
				pass

	#play(result)

	# get raw audio data as a bytestring
	raw_data = result.raw_data
	# get the frame rate
	sample_rate = result.frame_rate
	# get amount of bytes contained in one sample
	sample_size = result.sample_width
	# get channels
	channels = result.channels

	raw_nums = np.frombuffer(raw_data, dtype=np.int16)

	f = open("raw.dat","w")
	for i in raw_nums:
		f.write(str(int(i)))
		f.write("\n")
	f.close()
		

	print("")
	print(sample_rate)
	print(sample_size)
	print(channels)
	print(len(raw_data))




    # word = word_list[0][chunk:]
    # sentence = word[:len(word)-chunk]
    # for word in word_list[1:]:
    #     temp = word[chunk:]
    #     sentence += temp[:len(temp)-chunk]

	# morse_sound.export("morse_code.mp3", format="mp3")

	# vlc.play("/Users/griffin/Code/Courses/1-Current_Courses/4883-Software-Tools/Resources/morse_code/sentence.mp3")

	# message = "--. . . -.- ... -....- ..-. --- .-. -....- --. . . -.- ... "
	# result = decrypt(message) 
	# print (result) 

# Executes the main function 
if __name__ == '__main__': 
	main() 
