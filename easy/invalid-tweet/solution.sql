-- Solution for the 'Invalid Tweets' problem.
-- Write your PostgreSQL query statement below.

SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 15