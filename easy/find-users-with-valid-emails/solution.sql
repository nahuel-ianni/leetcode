-- Solution to the 'Find Users With Valid E-Mails' problem.
-- Write your PostgreSQL query statement below.

SELECT *
FROM Users
WHERE mail ~ '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$';