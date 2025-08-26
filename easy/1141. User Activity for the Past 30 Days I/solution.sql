-- Solution to the 'User Activity for the Past 30 Days I' problem.
-- Write your PostgreSQL query statement below.

SELECT activity_date AS day, COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date >= '2019-07-27'::date - INTERVAL '29 days'
    AND activity_date <= '2019-07-27'::date
GROUP BY activity_date;

-- Alternative: BETWEEN can be less performant than comparisons
-- SELECT activity_date AS day, COUNT(DISTINCT user_id) AS active_users
-- FROM Activity
-- WHERE activity_date BETWEEN '2019-07-27'::date - INTERVAL '29 days' AND '2019-07-27'
-- GROUP BY activity_date;