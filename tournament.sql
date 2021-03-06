-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
DROP DATABASE IF EXISTS tournament;

CREATE DATABASE tournament;
\c tournament;

--Table containing id's and names of players
CREATE TABLE players (
	id SERIAL PRIMARY KEY, 
	name TEXT);

--table of matches played listing winner and loser
CREATE TABLE matches (
	winner INTEGER REFERENCES players (id),
	loser INTEGER REFERENCES players (id),
	PRIMARY KEY (winner, loser)
);

--View for showing the number of games played by each player
CREATE VIEW games_played AS
SELECT players.id, count(matches.*) as matches
FROM players LEFT JOIN matches
ON matches.winner = players.id OR matches.loser = players.id
GROUP BY players.id;

--View for showing the number of games won by each player
CREATE VIEW games_won AS
SELECT players.id, count(matches.winner) as wins
FROM players LEFT JOIN matches
ON players.id = matches.winner
GROUP BY players.id
ORDER BY wins DESC;


