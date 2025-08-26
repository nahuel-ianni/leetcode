-- Solution to the 'Fix Names in a Table' problem.
-- Write your PostgreSQL query statement below.

SELECT user_id,
       UPPER(LEFT(name, 1)) || LOWER(SUBSTR(name, 2)) AS name
FROM Users
ORDER BY user_id;

-- INITCAP(name) AS name -> Capitalizes EACH word, rather than just the first one.