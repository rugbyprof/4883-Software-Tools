# -*- coding: UTF-8 -*-
import requests
import os,sys
from time import sleep
import pprint
import json
from time import sleep


def get_word(word,code):
    # create urls for british and us sound files
    url_filename = "{}--_{}_1.mp3".format(word,code)

    # create save location with name
    sav_filename = os.path.join("words_{}","{}_{}.mp3".format(code,word,code))

    url = "https://ssl.gstatic.com/dictionary/static/sounds/oxford/{}".format(url_filename) 

    try:
        r = requests.get(url)
        with open(sav_filename, 'wb') as f1:
            f1.write(r.content)
        with open('word_{}_urls.txt'.format(code), 'a') as f2:
            f2.write(url+"\n")    
    except requests.exceptions.Timeout:
        # Maybe set up for a retry, or continue in a retry loop
        pass
    except requests.exceptions.TooManyRedirects:
        # Tell the user their URL was bad and try a different one
        pass
    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        print(e)

    return os.path.isfile(sav_filename)

# vscode sets cwd as "folder opened by editor" so I'm changing it for local running
os.chdir('/Users/griffin/Code/Courses/1-Current_Courses/4883-Software-Tools/Resources/creepy')

# empty url lists
with open('word_gb_urls.txt', 'w') as f:
    f.write("") 
with open('word_us_urls.txt', 'w') as f:
    f.write("") 

# if clean dict doesn't exist, make it
if not os.path.isfile('dictionary_clean.json'):

    with open("dictionary.txt","r") as f:
        data = f.read()

    data = data.split("\n")

    unique = {}

    for word in data:
        word = word.strip()
        word = word.replace("'", "")
        word = word.lower()
        unique[word] = 1

    unique = list(unique.keys())

    with open('dictionary_clean.json', 'w') as f:
        f.write(json.dumps(unique))

# load clean dict into list
with open('dictionary_clean.json', 'r') as f:
    words = json.loads(f.read())

letter_counts = {}
total_words = 0
longest = 0

for word in words:
    total_words += 1
    if not word[0] in letter_counts:
        letter_counts[word[0]] = 0

    letter_counts[word[0]] += 1

    if len(word) > longest:
        longest = len(word)

# get british first to at least
# obtain 1 set

# total_count = 0
# letter_count = 0
# prev_letter = ''

# for word in words:
#     letter = word[0]

#     if letter != prev_letter:
#         letter_count = 0
    
#     letter_count += 1
#     total_count += 1

#     if get_word(word,'gb'):
#         print("{} {} {}".format(word.ljust(longest+2),round(letter_count/letter_counts[letter],3),round(total_count/total_words,3)))
#     else:
#         print("*** {} failed ***".format(word))

total_count = 0
letter_count = 0
prev_letter = ''

# get us words
for word in words:
    letter = word[0]

    if letter != prev_letter:
        letter_count = 0
        prev_letter = letter
    
    letter_count += 1
    total_count += 1

    if get_word(word,'us'):
        print("{} {} , {}".format(word.ljust(longest+2),round(float(letter_count)/float(letter_counts[letter]),5),round(float(total_count)/float(total_words),5)))
    else:
        print("*** {} failed ***".format(word))
