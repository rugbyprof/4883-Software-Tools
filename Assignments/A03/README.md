## Data Scraping - Beautiful Soup and NFL Data
### Due: Wed, February 6<sup>th</sup> and Wed, February 13<sup>th</sup>


#### Due Dates:
- Wednesday these files are due:
    - `scrape_game_ids.py`
    - `scrape_game_data.py`
- Friday your stats output and fully commented code is due.

## Background

### Overview

Using `python2` or `python3` and `beautifulsoup` obtain all of the NFL stats from 2009 until present by scraping both of the following:

- http://www.nfl.com/schedules/ 
- http://www.nfl.com/liveupdate/game-center/

Examples on how to scrape sites can be found [HERE](https://github.com/rugbyprof/4883-Software-Tools/tree/master/Resources/scraping) or on the web. 

The nfl liveupdate site will provide us with the stats, but it requires a specific game id. We get the game id's from nfl.com's schedule page. So lets start there.

### Schedule

Remember we need to leverage our knowledge of not only HTML, but also how a specific site uses thier URL. Look at the URL below:

```
http://www.nfl.com/schedules/2018/POST
```

With some knowledge of the NFL we can gleen a little info about this URL. Its probably for the 2018 season, and more specifically for the post season. If you go to the `nfl.com/schedules` page and choose different seasons as well as regular and post season we can see how the url changes:

```
http://www.nfl.com/schedules/2018/POST
http://www.nfl.com/schedules/2010/REG3
http://www.nfl.com/schedules/2014/REG15
```

The url basically has three important components: `year`, `season type` (PRE/POST), and `week`. Knowing this, we can build our URL like so:

```python
year = 2018
stype = "REG"
week = 15
url = "http://www.nfl.com/schedules/%d/%s%d" % (year,stype,week)

# or

year = 2016
stype = "POST"
week = "" # Not needed
url = "http://www.nfl.com/schedules/%d/%s%s" % (year,stype,str(week))

# How you handle strings and ints is up to you. It might be wise to cast all to 
# string so you can use the same business logic to build your URL everytime.

```

This gives us the knowledge to peruse the entire NFL's schedule for any year from now back to 1970. However, what we really want from `nfl.com` is a specific reference or identifier for each game. I know this from inspecting the second site we need: http://www.nfl.com/liveupdate/game-center/ .

### Next Step

Here is an example liveupdate URL: http://www.nfl.com/liveupdate/game-center/2009102505/2009102505_gtd.json

The value: `2009102505` seems to be a date: `2009/10/25` with the value `05` at the end. If you go back to nfl.com's schedule page and inspect the HTMl, we can find many of these values embedded within the HTML. Here is an example:

```html
<div class="schedules-list-content post expandable  type-reg pro-legacy" data-gameid="2014101908" data-away-abbr="TEN" data-home-abbr="WAS" data-away-mascot="Titans" data-home-mascot="Redskins" data-gamestate="POST" data-gc-url="http://www.nfl.com/gamecenter/2014101908/2014/REG7/titans@redskins" data-localtime="13:00:00" data-shareid="sb-xhku48a4" data-site="FedExField" id="yui_3_10_3_1_1548700659128_122">
```

The  html attribute: `data-gameid` gives us exactly what we need. 

### Finally

You can now build your liveupdate URL by plugging in `game-id`'s to the url:

```python
# Depending on how you store your game id's
igameid = 2009102505
sgameid = "2009102505"
url = "http://www.nfl.com/liveupdate/game-center/%d/%d_gtd.json" % (igameid)
# or
url = "http://www.nfl.com/liveupdate/game-center/%s/%s_gtd.json" % (sgameid)
```

### NFL Json

The NFL json files that you will scrape will contain a games worth of statistics. If you scrape all of the files from 2009 until present day you will have a complete set of statistics for the NFL from 2009 - 2018 (minus the Super Bowl this year). Here is a collapsed version of a game object:

```json
{
    "2009102505": {
        "home": {
            "score": {
                "1": 3,
                "2": 0,
                "3": 3,
                "4": 0,
                "5": 0,
                "T": 6
            },
            "abbr": "STL",
            "to": 3,
            "stats": {},      
            "players": null
        },
        "away": {
            "score": {
                "1": 14,
                "2": 7,
                "3": 7,
                "4": 14,
                "5": 0,
                "T": 42
            },
            "abbr": "IND",
            "to": 3,
            "stats": {},     
            "players": null
        },
        "drives": {},        
        "scrsummary": {},     
        "weather": null,
        "media": null,
        "yl": "",
        "qtr": "Final",
        "note": null,
        "down": 0,
        "togo": 0,
        "redzone": true,
        "clock": "00:17",
        "posteam": "STL",
        "stadium": null
    },
    "nextupdate": 258
}
```

- A summary of the game stats can be found in: `["2009102505"]["home" or "away"]["stats"]`.
- Individual player stats are located under `["2009102505"]["drives"][X]["plays"][Y]["players"]` where `X` = `drive-number` and `Y` = `play-id`.

Here is an example play in a drive. Each player involved in a play is listed in the "players" array. If the stat is associated with a player, then the players id will be the "key" to the stat, otherwise it will be an integer. The `statId` describes what they did. In this play we have three stats:

- `statId` : 3 = First down associated with no one.
- `statId` : 79 = Solo Tackle associated with "00-0023501" or "O.Atogwe"
- `statId` : 10 = Rushing Yards associated with "00-0024245" or "J.Addai"

```json
"3068": {
    "sp": 0,
    "qtr": 4,
    "down": 1,
    "time": "09:40",
    "yrdln": "IND 20",
    "ydstogo": 10,
    "ydsnet": 25,
    "posteam": "IND",
    "desc": "(9:40) J.Addai left tackle to IND 32 for 12 yards (O.Atogwe).",
    "note": null,
    "players": {
        "0": [{
            "sequence": 1,
            "clubcode": "IND",
            "playerName": "",
            "statId": 3,              
            "yards": 0
        }],
        "00-0023501": [{
            "sequence": 3,
            "clubcode": "STL",
            "playerName": "O.Atogwe",
            "statId": 79,             
            "yards": 0
        }],
        "00-0024245": [{
            "sequence": 2,
            "clubcode": "IND",
            "playerName": "J.Addai",
            "statId": 10,             
            "yards": 12             
        }]
    }
}
```

Notice that every play also has a `clubcode` so the cummulative team stats can be compiled.

## Assignment

### Stats to Find
1. Find the player(s) that played for the most teams.
2. Find the player(s) that played for multiple teams in one year.
3. Find the player(s) that had the most yards rushed for a loss.
4. Find the player(s) that had the most rushes for a loss.
5. Find the player(s) with the most number of passes for a loss.
6. Find the team with the most penalties.
7. Find the team with the most yards in penalties.
8. Find the correlation between most penalized teams and games won / lost.
9. Average number of plays in a game.
10. Longest field goal.
11. Most field goals.
12. Most missed field goals.
13. Most dropped passes (Search for "pass" and "dropped" in play description, and stat-id 115).

>NOTE: If any of the results returns more than 10 items, just provide the top 10. For example if #2 returns a lot of players then list the players that played for the most teams first and the remaining will be alphabetical. 

### Deliverables

- Create a folder called `A03` in your assignments folder.
- Create a `README.md` that lists all the files, a description of your project, and provides all necessary instructions for me to run your code.  
- At a minimum you should have two files that gather the information and they should be named:
    - `scrape_game_ids.py`
    - `scrape_game_data.py`
- Do not put all your scraped json files on github (unless you want to).
- Name your json files with the same convention I used: `gameid.json` (e.g. `2014110901.json`) that way I can run your code on my local files.
- If your code uses data structures that you created and saved to a file, those should be either uploaded or provided to me with instructions on how to create them.
- In addition to the two scraping files, there should be one more called `calculate_stats.py` that I can run which will provide the answers to the above stat questions. It should create an output file that clearly portrays which question is being answered, along with your calculated answer (see below).
- Your code should be organized with functions, preferrably one function per stat to find. Each function should be commented (see below).


#### Example Output
```
Name: your name
Assignment: A03 - Nfl Stats 
Date: the date

==================================================================================
1. Find the player(s) that played for the most teams.

Answer:

Player 1 played for X teams.
Player 2 played for X teams.

...

==================================================================================
11. Most field goals.

Player A. Smith made XX fields goals.
```

### Example Comments


### File Comment
```python
"""
Course: cmps 4883
Assignemt: A03
Date: 2/04/19
Github username: dorknuts
Repo url: https://github.com/yourgithubusername/reponame
Name: John Magee
Description: 
    A small description of the program ....

"""

```

#### Function or Class Comment

```python
##############################################################
# calculateMostFieldGoals(p1,p2,...)
# This function does something to be described here...
# 
# Params: 
#    p1 [type] : description
#    p2 [type] : description 
#    etc
# Returns: 
#    What it returns and its type
def calculateMostFieldGoals(p1,p2,p3):
  # function body here...
```
