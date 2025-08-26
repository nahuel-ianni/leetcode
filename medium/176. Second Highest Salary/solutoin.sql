-- Solution to the 'Second Highest Salary' problem.
-- Write your PostgreSQL query statement below.

-- Wrapped in a SELECT to ensure the 'null' value is returned.
SELECT (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
) AS SecondHighestSalary

-- SELECT MAX(salary) AS "SecondHighestSalary" FROM Employee 
-- WHERE salary != (
--     SELECT MAX(salary) FROM Employee
-- );