from beautifulscraper import BeautifulScraper
from pprint import pprint
from time import sleep
import json
import urllib

# scraper = BeautifulScraper()

# years  = [x for x in range(2009,2019)]
# years  = [x for x in range(2009,2012)]

# weeks = [x for x in range(1,18)]
# weeks = [x for x in range(1,5)]

# stype = "REG"

# gameids = {
#     "REG":{},
#     "POST":{}
#     }

# for year in years:
#     gameids["REG"][year] = {}
#     for week in weeks:
#         gameids["REG"][year][week] = []
#         url = "http://www.nfl.com/schedules/%d/%s%s" % (year,stype,str(week))

#         print(url)
#         page = scraper.go(url)

#         divs = page.find_all('div',{"class":"schedules-list-content"})

#         for div in divs:
#             gameids["REG"][year][week].append(div['data-gameid'])
#         sleep(.02)

#     gameids["POST"][year] = []
#     url = "http://www.nfl.com/schedules/%d/%s" % (year,"POST")
#     print(url)
#     page = scraper.go(url)

#     divs = page.find_all('div',{"class":"schedules-list-content"})

#     for div in divs:
#         gameids["POST"][year].append(div['data-gameid'])
#     sleep(.02)


# pprint(gameids)
# pprint(gameids.keys())

# for year in gameids:
#     print(gameids[year].keys())

# f = open("nfldata.json","w")

# f.write(json.dumps(gameids))
# f.close()

if __name__=='__main__':

    with open('nfldata.json') as f:
        data = json.load(f)

    for season_type,subdictionary in data.items():
        print(season_type)
        if season_type == "REG":
            for year,week_dictionary in subdictionary.items():
                print(year)
                for week,gameids in week_dictionary.items():
                    print(week)
                    for game in gameids:
                        print(game)
                
        else:
            for year,gameids in subdictionary.items():
                print(year)
                for game in gameids:
                    print(game)
                    print("http://www.nfl.com/liveupdate/game-center/%s/%s_gtd.json" % (game,game))
                    url = "http://www.nfl.com/liveupdate/game-center/%s/%s_gtd.json" % (game,game)
                    urllib.request.urlretrieve(url,'nfl_data/'+game+'.json')
