-- Solution to the 'Game Play Analysis IV' problem.
-- Write your PostgreSQL query statement below.

SELECT ROUND(
    COUNT(*)::NUMERIC / 
    (SELECT COUNT(DISTINCT player_id) FROM Activity), 
    2
) AS fraction
FROM Activity A
WHERE (A.player_id, A.event_date-1) IN (
    SELECT player_id, MIN(event_date)
    FROM Activity
    GROUP BY player_id
);

-- Alternative
-- SELECT ROUND(
--     -- Find users who logged in on the day AFTER their first login
--     COUNT(DISTINCT CASE 
--         WHEN A1.event_date = (
--             SELECT MIN(event_date) 
--             FROM Activity A2 
--             WHERE A2.player_id = A1.player_id
--         ) + INTERVAL '1 day' 
--         THEN A1.player_id 
--         END) /
--     -- Find unique players
--     (SELECT COUNT(DISTINCT player_id) FROM Activity)::NUMERIC,
--     2
-- ) AS fraction
-- FROM Activity A1;