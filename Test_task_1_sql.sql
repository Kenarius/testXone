SELECT client_number as client,
COUNT(case outcome WHEN 'win' THEN 1 ELSE NULL END) as win,
COUNT(case outcome WHEN 'lose' THEN 1 ELSE NULL END) AS lose
FROM bid
INNER JOIN event_value
ON bid.play_id = event_value.play_id AND bid.coefficient = event_value.value 
GROUP BY client_number;