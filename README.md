#Tournament Results
Project for Udacity Fullstack Nanodegree.
Python application that utilizes PostgreSQL to keep track of players in Swiss style tournament
##How to use
* This application requires you to install Python, psycopg and PostgreSQL.
* Initialize database, tables and views using script in tournament.sql.
* Use `deleteMatches()` and `deletePlayers()` functions to ensure a clear database.
* Add players using `registerPlayer(name)` function, they will be assigned an id number.
* Use `countPlayers()` after all players are added to check for the correct number
* report each match with `reportMatch(winner, loser)` after each match
* Use `swissPairings()` to get new matchups after all matches from the previous round are complete 

