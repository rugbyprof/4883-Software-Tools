## Intro to Sql - NFL Stat Mining using Sql
### Due: Wednesday February 20<sup>th</sup>


### Overview

Processing `json` files can be tedious work, especially large complex ones. Another software tool that can make the task of aggregating data much much easier is `SQL`. This is not a database class, but running some simple queries is not beyond the scope of our skills. 

The questions below are the same questions I asked you to calculate processing your 2000+ `json` files we acquired from the NFL. Lets see how much easier it can be if we use `SQL` to get it done. 

#### Old Requirements 

- Count number of teams a player played for.
- Find the top 5 rushing players per year.
- Find the bottom 5 passing players per year.
- Find the top 5 that had the most rushes for a loss.
- Find the top 5 teams with the most penalties.
- Find the average number of penalties per year.
- Find the average number of plays in a game.
- Find the top 5 players that had field goals over 40 yards.
- Top 5 Most missed field goals.

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

