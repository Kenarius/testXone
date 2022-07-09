SELECT fight.game, count(*) AS games_count
FROM (SELECT concat(least(home_team, away_team), '-', greatest(home_team, away_team)) AS game
FROM event_entity) AS fight
GROUP BY game
ORDER BY games_count;