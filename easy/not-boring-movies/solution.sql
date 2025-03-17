-- Solution for the 'Not Boring Movies' problem.
-- Write your PostgreSQL query statement below.

SELECT *
FROM Cinema
WHERE description != 'boring' AND MOD(id, 2) != 0
ORDER BY rating DESC;

-- SELECT *
-- FROM Cinema
-- WHERE description <> 'boring' AND id%2 <> 0
-- ORDER BY rating DESC;