-- Solution to the 'Primary Department for Each Employee' problem.
-- Write your PostgreSQL query statement below.

SELECT DISTINCT ON (employee_id) employee_id, department_id
FROM Employee
ORDER BY employee_id, (primary_flag = 'Y') DESC;

-- Alternative
-- SELECT employee_id, department_id
-- FROM (
--     SELECT *, COUNT(*) OVER (PARTITION BY employee_id) AS dept_count
--     FROM Employee
-- ) T
-- WHERE primary_flag = 'Y' OR (primary_flag = 'N' AND dept_count = 1);