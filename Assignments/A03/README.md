## Data Scraping - Beautiful Soup and NFL Data
### Due: Wednesday February 6<sup>th</sup> by classtime

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

### Nfl Json


## Assignment

