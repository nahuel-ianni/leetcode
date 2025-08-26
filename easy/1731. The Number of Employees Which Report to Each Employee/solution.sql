-- Solution to the 'The Number of Employees Which Report to Each Employee' problem.
-- Write your PostgreSQL query statement below.

 SELECT 
    M.employee_id,
    M.name,
    COUNT(E.reports_to) AS reports_count,
    ROUND(AVG(E.age)) AS average_age
 FROM Employees M
 JOIN Employees E ON M.employee_id = E.reports_to
 GROUP BY M.employee_id, M.name
 ORDER BY M.employee_id