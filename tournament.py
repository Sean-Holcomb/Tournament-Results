#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection, a cursor."""
    db = psycopg2.connect("dbname=tournament")
    cursor = db.cursor()
    return db, cursor


def deleteMatches():
    """Remove all the match records from the database."""
    conn, cursor = connect()
    cursor.execute("TRUNCATE matches")
    conn.commit()
    conn.close()


def deletePlayers():
    """Remove all the player records from the database."""
    conn, cursor = connect()
    cursor.execute("TRUNCATE players CASCADE")
    conn.commit()
    conn.close()


def countPlayers():
    """Returns the number of players currently registered."""
    conn, cursor = connect()
    cursor.execute("SELECT count(*) AS num FROM players")
    count = cursor.fetchone()
    print(count)
    conn.close()
    return count[0]


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    conn, cursor = connect()
    query = "INSERT INTO players (name) VALUES (%s) "
    param = [name]
    cursor.execute(query, param)
    conn.commit()
    conn.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn, cursor = connect()
    cursor.execute("SELECT players.id, players.name, games_won.wins, games_played.matches FROM players, games_won, games_played WHERE players.id = games_won.id and players.id = games_played.id ORDER BY games_won.wins desc")
    rows = cursor.fetchall()
    standings = [(row[0], row[1], row[2], row[3]) for row in rows]
    conn.close()
    print(standings)
    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn, cursor = connect()
    query = "INSERT INTO matches (winner, loser) VALUES (%s, %s)"
    param = (winner, loser)
    cursor.execute(query, param)
    conn.commit()
    conn.close()
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    standings = playerStandings()
    conn, cursor = connect()
    cursor.execute("SELECT * FROM matches")
    matches = cursor.fetchall()
    conn.close()
    pairings = []
    hasPlayed = False
    matched = []
    #algorithm to prevent repeat matches
    #loop through every player in standings except the last
    for i in range(len(standings)-1):
        #check if index i has already been match if so skip to the next cycle
        if i in matched:
            continue
        #loop through all players in standing after i's index
        for k in range(i+1, len(standings)):
            #check if index k has already been match if so skip to the next cycle
            if k in matched:
                continue
            #reset boolean for checking if two players have already played    
            hasPlayed = False
            #Check previous matches for cases when players at i and k have played before
            for j in matches:
                if (standings[i][0] == j[0] and standings[k][0] == j[1]) or (standings[i][0] == j[1] and standings[k][0] == j[0]):
                    hasPlayed = True
            #if the have not played, pair them and add index i and k to the list for skipping
            if not hasPlayed:
                pair = (standings[i][0], standings[i][1], standings[k][0], standings[k][1])
                pairings.append(pair)
                matched.append(i)
                matched.append(k)
                break
    return pairings
