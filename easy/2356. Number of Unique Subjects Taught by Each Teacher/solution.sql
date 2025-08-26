-- Solution to the 'Number of Unique Subjects Taught by Each Teacher' problem.
-- Write your PostgreSQL query statement below.

SELECT teacher_id, COUNT(DISTINCT subject_id) AS cnt
FROM Teacher
GROUP BY teacher_id