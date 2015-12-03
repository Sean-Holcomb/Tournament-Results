#Tournament Results
Project for Udacity Fullstack Nanodegree.
Python application that utilizes PostgreSQL to keep track of players in Swiss style tournament
##How to install
1. Install Virtual Box and Vagrant using these <a href = https://www.udacity.com/wiki/ud197/install-vagrant>instruction</a> and the provided config file
2. Navigate to the the repository you just cloned and replace the tournament dirrectory with this repository.
3. From the command line navigate to the vagrant file and type the following commands:

	```
	vagrant up

	vagrant ssh

	cd /vagrant/tournament
	```
	
4. Next create the database by entering `psql` and copy and paste the contents of tournament.sql into the terminal.
5. If all tables and views were added with no error, use control-d to exit psql
6. Run `python tournament_test.py` if all 8 test pass then the program is running properly.

##Usage
* Use `deleteMatches()` and `deletePlayers()` functions to ensure a clear database.
* Add players using `registerPlayer(name)` function, they will be assigned an id number.
* Use `countPlayers()` after all players are added to check for the correct number
* report each match with `reportMatch(winner, loser)` after each match
* Use `swissPairings()` to get new matchups after all matches from the previous round are complete 

