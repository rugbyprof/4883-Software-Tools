from pydub import AudioSegment
import sys
import os
import vlc


def kvargs(sysargs):
    kvargs = {}
    args = []

    # traverse copy of sys.argv skipping first element
    for val in sysargs[1:]:
        if '=' in val:
            k,v = val.split('=')
            args[k] = v
        else:
            args.append(val)
    return args,kvargs

def usage(e):
    print("Do it right. \n {}".format(e))
    sys.exit()

if __name__=='__main__':

    words,kvargs = kvargs(sys.argv)

    if "output_file" in kvargs:
        output_file = kvargs['output_file']
    else:
        output_file = 'output.mp3'

    if len(words) == 0:
        usage()
    
    word_list = []

    print(words)

    for word in words:
        if os.path.isfile(word):
            word_list.append(AudioSegment.from_mp3(word))
        else:
            usage("Word is not a valid path to mp3!")

    # Concatenation is just adding
    chunk = 100
    word = word_list[0][chunk:]
    sentence = word[:len(word)-chunk]
    for word in word_list[1:]:
        temp = word[chunk:]
        sentence += temp[:len(temp)-chunk]

    # writing mp3 files is a one liner
    sentence.export("sentence.mp3", format="mp3")

    vlc.play("/Users/griffin/Code/Courses/1-Current_Courses/4883-Software-Tools/Resources/morse_code/sentence.mp3")