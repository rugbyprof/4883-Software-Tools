## Intro to Sql - NFL Stat Mining using Sql
### Due: Friday February 29<sup>th</sup>

### Overview

Processing `json` files can be tedious work, especially large complex ones. Another software tool that can make the task of aggregating data much much easier is `SQL`. This is not a database class, but running some simple queries is not beyond the scope of our skills. 

The questions below are the same questions I asked you to calculate processing your 2000+ `json` files we acquired from the NFL. Lets see how much easier it can be if we use `SQL` to get it done. 

### VSCode

https://github.com/rugbyprof/4883-Software-Tools/tree/master/Resources/vscode_and_sftp

#### Requirements 

**Q1**
- Count number of teams an individual player played for.
- Limit your output to the top 10 players that played for the most teams.
- Output

```
Teams played for:

#     PlayerID      Name          # Teams
=========================================
1     00-00001234   D. Smith         #
2         ''           ''            ''
3         ''           ''            ''
```

**Q2**
- Find the players with the highest total rushing yards by year, and limit the result to top 5.
- This means to sum up all players rushing yards per year, and list the top 5 (most yards) in your output.
- Output

```
Top 5 rushing players:

#     PlayerID      Name        Year    # Yards
================================================
1     00-00001234   D. Smith    2010      ####
2     00-00005678   E. Hall     2017      ####
3     00-00003333   T. Brad     2012      ####
4     00-00001255   M. Turk     2010      ####
4     00-00002266   Z. Zoro     2013      ####
```

**Q3**
- Find the bottom 5 passing players per year.
- This is the similar to previous question, just change top to bottom, and most to least.
- Output

```
Bottom 5 passing players:

#     PlayerID      Name        Year    # Yards
================================================
1     00-00001234   D. Xxxx     2018      ####
2     00-00005678   E. Bbbb     2014      ####
3     00-00003333   T. Mmmm     2014      ####
4     00-00001255   M. Aaaa     2010      ####
4     00-00002266   Z. Pppp     2012      ####
```

**Q4**
- Find the top 5 players that had the most rushes for a loss.
- This is not grouped by year, this is over a players career.
- Output: Formatted same as previous 

**Q5**
- Find the top 5 teams with the most penalties.
- This is not grouped by year, this is over a players career.
- Output: Formatted same as previous

**Q6**
- Find the average number of penalties per year.
- Average Penalties = Sum of all penalties per year / Total games played that year
- Output: List the top 10 seasons by highest average number of penalties.

```
Average Penalties Per Year:

#     Season     Total Penalties   Avg Penalties
================================================
1     2009         ####                 ###
2     2010          ''                  ''
3      ''           ''                  ''
...
10    2018         ####                 ###
```

**Q7**
- Find the Team with the least amount of average plays every year.
- Average Plays is by game.
- Total Plays is per year. 
- Output: List the top 10 teams by lowest average number of plays.

```
Average number of plays in a game:

#     Team         Season             Avg Plays
================================================
1     ARI          2009                 ###
2     NE           2010                 ###
3     NO           2011                 ###
4     DAL          2012                 ###
                      ...
10    OAK          2018                 ###
```

**Q8**
- Find the top 5 players that had field goals over 40 yards.
- Output: you have an idea

**Q9**
- Find the top 5 players with the shortest avg field goal length.
- Output: you have an idea

**Q10**
- Rank the NFL by win loss percentage (worst first).
```
NFL by win/loss percentage:

#     Team         Won/Loss %
================================================
32     ???           ###
31     ???           ###
30     ???           ###
29     ???           ###
...
```
    
**Q11**
- Find the top 5 most common last names in the NFL.
```
Common Names:

#     Name         Occurences
================================================
1     ???           ###
2     ???           ###
3     ???           ###
4     ???           ###
5     ???           ###
...
```

### Bonus

**QB1**
- Find average penalties per week (NFL wide). (They should go down?)

```
Year        w1   w2   w3 ...   w17
================================================
2009       ###  ###  ###      ###
2010       ###  ###  ###      ###
...
2018       ###  ###  ###      ###
```

**QB2**
- Find the most penalized players.

```
Year       ARI / Pen#       ATL / Pen#    BAL / Pen#   ...    TB / Pen#       TEN / Pen#       WAS / Pen#
=========================================================================================================
2009       ???????/##.#     ???????/##.#  ???????/##.#        ???????/##.#    ???????/##.#?    ???????/##.#
2010       ???????/##.#     ???????/##.#  ???????/##.#        ???????/##.#    ???????/##.#?    ???????/##.#
...
2018       ???????/##.#     ???????/##.#  ???????/##.#        ???????/##.#    ???????/##.#?    ???????/##.#
```

**QB3**
- Find the best 'away' team for every year Where away percentage is = ` away wins / away total games`. (Table: `games` column: `win_type`)

```
Year       Team     Away %
================================================
2009       ???      ###.#
2010       ???      ###.#
...
2018       ???      ###.#
```

- Find the highest and lowest scoring teams per year with their record.
- Find the player(s) with the least and most tackles (any kind) and least per team per year.

### Extra Bonus

**QBB!!**
- Find the best defense in the NFL (per year) where "best" could be defined as:
    - They minimized offensive total yards
    - Maximized offensive turnovers
    - Maximized offensive penalties
    - Minimized offensive time of possession (TOP)
    - Maximized defensive scoring

### PHP YaY!

- [driver.php](./driver.php)
- [get_players1.php](./get_players1.php)
- [get_players2.php](./get_players2.php)
- [load_stat_codes.php](./load_stat_codes.php)
- [query_function.php](./query_function.php)

#### Example Output

- Same as for A04.
- Make sure you use strpad to line up your columns
- Header below, and use examples above as your guideline.

```
Name: your name
Assignment: A04 - Nfl Stats 
Date: the date

==================================================================================



```

### Deliverables

- Folder `A04` in your repo.
- All php files in your `A04` folder.
- All php files appropriately commented.
- Properly formatted output file. 
- `README.md` with:
  - project overview (description)
  - list of files, 
  - file descriptions, 
  - any instructions needed to run or help grade your project
