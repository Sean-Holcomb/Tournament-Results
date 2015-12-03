-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE DATABASE tournament;
\c tournament;

CREATE TABLE players (
	id SERIAL PRIMARY KEY, 
	name TEXT);

CREATE TABLE matches (
	player1 INTEGER, 
	player2 INTEGER, 
	winner INTEGER);

CREATE VIEW games_played AS
SELECT players.id, count(matches.*)
FROM players, matches
WHERE matches.* = players.id
GROUP BY players.id

CREATE VIEW games_won AS
SELECT player.id, count(matches.winner)
FROM players, matches
WHERE player.id = matches.winner
GROUP BY players.id


