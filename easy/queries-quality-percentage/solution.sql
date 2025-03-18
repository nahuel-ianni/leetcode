-- Solution to the 'Queries Quality and Percentage' problem.
-- Write your PostgreSQL query statement below.

SELECT
    query_name,
    ROUND(AVG((rating / position::NUMERIC)), 2) AS quality,
    ROUND(AVG((rating < 3)::INT) * 100, 2) AS poor_query_percentage
FROM Queries
GROUP BY query_name;