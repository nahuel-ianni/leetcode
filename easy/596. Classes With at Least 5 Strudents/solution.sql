-- Solution to the 'Classes More Than 5 Students' problem.
-- Write your PostgreSQL query statement below.

SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(class) >= 5