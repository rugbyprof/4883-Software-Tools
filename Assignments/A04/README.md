## Intro to Sql - NFL Stat Mining using Sql
### Due: Wednesday February 25<sup>th</sup>

# Making formatting changes and some SQL changes, will be done by close of business Feb 21st

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
    
- Top 5 Most missed field goals.
    - Output: you have an idea
- Find the top 5 most common last names in the NFL.

### PHP YaY!

- [driver.php](./driver.php)
- [get_players1.php](./get_players1.php)
- [get_players2.php](./get_players2.php)
- [load_stat_codes.php](./load_stat_codes.php)
- [query_function.php](./query_function.php)

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

