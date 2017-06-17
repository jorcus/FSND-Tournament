#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""

    return psycopg2.connect('dbname=tournament')


def deleteMatches():
    """Remove all the match records from the database."""

    DB = connect()
    c = DB.cursor()
    query = 'DELETE FROM Match'
    c.execute(query)
    DB.commit()
    DB.close()


def deletePlayers():
    """Remove all the player records from the database."""

    DB = connect()
    c = DB.cursor()
    query = 'TRUNCATE Players CASCADE'
    c.execute(query)
    DB.commit()
    DB.close()


def countPlayers():
    """Returns the number of players currently registered."""

    DB = connect()
    c = DB.cursor()
    query = 'SELECT COUNT(*) FROM Players'
    c.execute(query)
    rows = c.fetchone()[0]
    DB.close
    return rows


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """

    DB = connect()
    c = DB.cursor()
    name = name
    c.execute('INSERT INTO Players (NAME) VALUES (%s)', (name,))
    DB.commit()
    DB.close()


def playerStandings():
    """Returns a list of (id, name, wins, matches) for each player,
    sorted by the number of wins each player has."""

    DB = connect()
    c = DB.cursor()
    query = 'SELECT * FROM playerStandings;'
    c.execute(query)
    rows = c.fetchall()
    DB.close()
    return rows


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players."""

    DB = connect()
    c = DB.cursor()
    c.execute('INSERT INTO match (winner, loser) VALUES (%s, %s)',
              (winner, loser))
    DB.commit()
    DB.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match."""

    rows = playerStandings()
    pairings = []
    count = len(rows)

    # Count rows and increment by 2 for pairing using range.
    # Include Name & id columns.

    for i in range(0, count, 2):
        paired_list = (rows[i][0],
                       rows[i][1],
                       rows[i + 1][0],
                       rows[i + 1][1])
        pairings.append(paired_list)

    return pairings
