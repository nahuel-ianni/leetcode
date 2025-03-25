-- Solution to the 'Triangle Judgement' problem.
-- Write your PostgreSQL query statement below.

SELECT
    *,
    CASE 
        WHEN ABS(x + y) > ABS(z) AND ABS(x + z) > ABS(y) AND ABS(y + z) > ABS(x)
        THEN 'Yes'
        ELSE 'No'
    END AS triangle
FROM Triangle