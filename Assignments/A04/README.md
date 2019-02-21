## Intro to Sql - NFL Stat Mining using Sql
### Due: Wednesday February 27<sup>th</sup>

### Overview

Processing `json` files can be tedious work, especially large complex ones. Another software tool that can make the task of aggregating data much much easier is `SQL`. This is not a database class, but running some simple queries is not beyond the scope of our skills. 

The questions below are the same questions I asked you to calculate processing your 2000+ `json` files we acquired from the NFL. Lets see how much easier it can be if we use `SQL` to get it done. 

#### Requirements 

- Count number of teams a player played for.
    - Output

```
Teams played for:

#     PlayerID      Name          # Teams
=========================================
1     00-00001234   D. Smith         #
2         ''           ''            ''
3         ''           ''            ''
```

- Find the top 5 rushing players per year.
    - Output

```
Top 5 rushing players:

#     PlayerID      Name        Year    # Yards
================================================
1     00-00001234   D. Smith    2011      ####
2         ''           ''                  ''
3         ''           ''                  ''
```

- Find the bottom 5 passing players per year.
    - Output

```
Bottom 5 passing players:

#     PlayerID      Name        Year    # Yards
================================================
1     00-00001234   D. Smith    2011      ####
2         ''           ''                  ''
3         ''           ''                  ''
```

- Find the top 5 players that had the most rushes for a loss.
    - Output: Same as previous 

- Find the top 5 teams with the most penalties.
    - Output: Same as previous 
    
- Find the average number of penalties per year.
    - Output:

```
Bottom 5 passing players:

#     Season     Total Penalties   Avg Penalties
================================================
1     2009         ####                 ###
2     2010          ''                  ''
3      ''           ''                  ''
...
10    2018         ####                 ###
```

- Find the Team with the least amount of average plays every year.
    - Output (Not accurate I made up values)
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
    
- Find the top 5 players that had field goals over 40 yards.
    - Output: you have an idea
    
- Find the top 5 players with the shortest avg field goal length.
    - Output: you have an idea
    
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

#### Bonus

- Find average penalties per week (NFL wide). (They should go down?)
- Find the most penalized players.
- Find the best 'away' team for every year. (Table: `games` column: `win_type`)
- Find the highest and lowest scoring teams per year.
- Find the most mentioned player (stats, penalties, etc.) (I'm guessing a quarterback).
- Find the player with the most solo tackles (per year).


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

