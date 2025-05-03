-- Solution to the 'Fix Names in a Table' problem.
-- Write your PostgreSQL query statement below.

SELECT user_id,
       UPPER(LEFT(name, 1)) || LOWER(SUBSTR(name, 2)) AS name
FROM Users
ORDER BY user_id;