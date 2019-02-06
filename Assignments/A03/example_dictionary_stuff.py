import os,sys
import json
import pprint as pp
import ujson

"""
Returns a list of files in given directory
"""
def getFiles(path):
    files = []
    for dirname, dirnames, filenames in os.walk(path):
        # print path to all subdirectories first.
        # for subdirname in dirnames:
        #     print(os.path.join(dirname, subdirname))

        # print path to all filenames.
        for filename in filenames:
            #print(os.path.join(dirname, filename))
            files.append(os.path.join(dirname, filename))

        # Advanced usage:
        # editing the 'dirnames' list will stop os.walk() from recursing into there.
        if '.git' in dirnames:
            # don't go into any .git directories.
            dirnames.remove('.git')
    return files

"""
Checks to see if it is json
"""
def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True

"""
Tries to open a file 
"""
def openFileJson(path):
    try:
      f = open(path, "r")
      data = f.read()
      if is_json(data):
          return json.loads(data)
      else:
          print "Error: Not json."
          return {}
    except IOError:
        print "Error: Game file doesn't exist."
        return {}

def getSeason(game_id):
    year = game_id[:4]
    month = game_id[4:6]
    if int(month) == 1 or int(month) == 2:
        return int(year) - 1
    else:
        return int(year)

path = '../json_data/live_update_data'
files = getFiles(path)

files = sorted(files)

rushingData = {}
oldSeason = 0

i = 0

# loop through files
for file in files:
    i += 1
    # read in json data and convert to dictionary
    data = openFileJson(file)

    # pull out the game id and game data
    for gameid,gamedata in data.items():
        if gameid != "nextupdate":
            season = getSeason(gameid)
            if season != oldSeason:
                rushingData[season] = {}
                oldSeason = season
            # go straight for the drives
            for driveid,drivedata in gamedata['drives'].items():
                #print(driveid)
                if driveid != 'crntdrv':
                    for playid,playdata in drivedata['plays'].items():
                        for playerid,play in playdata['players'].items():
                            if '-' in playerid:
                                for p in play:
                                    if p['statId'] == 10:
                                        if not playerid in rushingData[season]:
                                            rushingData[season][playerid] = {}
                                            rushingData[season][playerid]['info'] = p
                                            rushingData[season][playerid]['yards'] = []
                                        
                                        rushingData[season][playerid]['yards'].append(p['ya
with open('rushing.json', 'wb') as fp:
    ujson.dump(rushingData, fp)
sys.exit()
for season,seasonData in rushingData.items():
    print(season)
    for playerid,playerlist in seasonData.items():
        print(playerid)
        print(len(playerlist))


                


