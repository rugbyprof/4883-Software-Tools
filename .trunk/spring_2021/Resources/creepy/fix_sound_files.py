import glob
import sys
import os

os.chdir("/Users/griffin/Code/Courses/1-Current_Courses/4883-Software-Tools/Resources/creepy")


# codes = ['us','gb']

# for code in codes:
#     for i in range(26):
#         d = chr(i+65)
#         if not os.path.isdir('./words_{}/{}'.format(code,d)):
#             print("Making dir: ./words_{}/{}".format(code,d))
#             os.mkdir( './words_{}/{}'.format(code,d))

files = glob.glob('./words_gb/*.mp3')

for fpath in files:
    name = os.path.basename(fpath)
    for i in range(26):
        d = chr(i+65)
        l = chr(i+97)
        if l in name[0]:
            if 'us' in name:
                if os.path.isfile(fpath):
                    os.rename(fpath, './words_us/{}/{}'.format(d,name))
                    print("moving: {}, './words_us/{}/{}'".format(fpath,d,name))
            if 'gb' in name:
                if os.path.isfile(fpath):
                    os.rename(fpath, './words_gb/{}/{}'.format(d,name))
                    print("moving: {}, './words_gb/{}/{}'".format(fpath,d,name))
