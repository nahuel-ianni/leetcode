-- Solution for the 'Find Customer Referee' problem.
-- Write your PostgreSQL query statement below.

SELECT Customer.name 
FROM Customer 
WHERE referee_id != 2 OR referee_id IS NULL

-- Alternative version
-- SELECT name 
-- FROM Customer
-- WHERE COALESCE(referee_id, 0) != 2