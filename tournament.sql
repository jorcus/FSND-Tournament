DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
-- Connect to the newly created DB
\c tournament;


CREATE TABLE Players(
				id SERIAL PRIMARY KEY,
				name TEXT);

CREATE TABLE match(
				id SERIAL PRIMARY KEY,
				loser INT NOT NULL DEFAULT 0 REFERENCES Players(id),
				winner INT NOT NULL DEFAULT 0 REFERENCES Players(id));

CREATE VIEW playerStandings AS SELECT Players.id, Players.name,
(SELECT count(*) FROM match WHERE match.winner = Players.id ) as won,
(SELECT count(*) FROM match WHERE Players.id in (winner, loser)) as played
FROM Players GROUP BY Players.id ORDER BY won DESC;