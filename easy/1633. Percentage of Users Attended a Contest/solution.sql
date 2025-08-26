-- Solution to the 'Percentage of Users Attended a Contest' problem.
-- Write your PostgreSQL query statement below.

SELECT
    R.contest_id,
    ROUND(
        (COUNT(R.user_id) / (SELECT COUNT(*) FROM Users)::NUMERIC) * 100,
        2
    ) AS percentage
FROM Register R
GROUP BY R.contest_id
ORDER BY percentage DESC, R.contest_id;

-- Alternative
-- WITH total_users AS (
--     SELECT COUNT(*)::NUMERIC FROM Users
-- )
-- SELECT
--     R.contest_id,
--     ROUND((COUNT(R.user_id) / T.count) * 100, 2) AS percentage
-- FROM Register R
-- JOIN total_users T ON TRUE
-- GROUP BY R.contest_id, T.count
-- ORDER BY percentage DESC, R.contest_id;