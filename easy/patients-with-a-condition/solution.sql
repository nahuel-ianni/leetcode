-- Solution to the 'Patients With a Condition' problem.
-- Write your PostgreSQL query statement below.

SELECT *
FROM Patients
WHERE REGEXP_LIKE(conditions, 'DIAB1');

-- The following check ONLY if the first word begins with DIAB1.
-- WHERE LEFT(conditions, 5) = 'DIAB1';
-- WHERE conditions ^@ 'DIAB1';
-- WHERE STARTS_WITH(conditions, 'DIAB1');