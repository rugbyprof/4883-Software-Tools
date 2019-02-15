## Intro to Sql - NFL Stat Mining using Sql
### Due: Wednesday February 20<sup>th</sup>


### Overview

Processing `json` files can be tedious work, especially large complex ones. Another software tool that can make the task of aggregating data much much easier is `SQL`. This is not a database class, but running some simple queries is not beyond the scope of our skills. 

The questions below are the same questions I asked you to calculate processing your 2000+ `json` files we acquired from the NFL. Lets see how much easier it can be if we use `SQL` to get it done. 

#### Old Requirements 

- Find the player(s) that played for the most teams.
- Find the player(s) that played for multiple teams in one year.
- Find the player(s) that had the most yards rushed for a loss.
- Find the player(s) that had the most rushes for a loss.
- Find the player(s) with the most number of passes for a loss.
- Find the team with the most penalties.
- Find the team with the most yards in penalties.
- Find the correlation between most penalized teams and games won / lost.
- Average number of plays in a game.
- Longest field goal.
- Most field goals.
- Most missed field goals.
- Most dropped passes (Search for "pass" and "dropped" in play description, and stat-id 115).

#### New Requirements

- Find the game with the largest total yards (passing and rushing)
  - Print out the Season, Home Team, Away Team, Passing, Rushing, Total (Passing + Rushing)
- Find the top 5 players that had the most yards rushed for a loss in a single season.
  - Print out the Player Name, Season, and Yards Rushed 




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

