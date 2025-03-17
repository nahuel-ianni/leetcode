-- Solution to the 'Confirmation Rate' problem.
-- Write your PostgreSQL query statement below.

SELECT 
    S.user_id,
    ROUND(AVG(CASE WHEN C.action = 'confirmed' THEN 1 ELSE 0 END), 2) AS confirmation_rate
FROM Signups S
LEFT JOIN Confirmations C ON S.user_id = C.user_id
GROUP BY S.user_id;

-- WITH X AS (
--     SELECT 
--         user_id,
--         COUNT(*) AS T,
--         COUNT(*) FILTER (WHERE action = 'confirmed') AS C
--     FROM Confirmations
--     GROUP BY user_id
-- )
-- SELECT S.user_id, ROUND(COALESCE(X.C::NUMERIC / X.T, 0), 2) AS confirmation_rate
-- FROM Signups S
-- LEFT JOIN X ON S.user_id = X.user_id;