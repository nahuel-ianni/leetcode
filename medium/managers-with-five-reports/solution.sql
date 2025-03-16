-- Solution to the 'Managers with at Least 5 Direct Reports' problem.
-- Write your PostgreSQL query statement below.

SELECT E.name
FROM Employee E
JOIN (
    SELECT managerId
    FROM Employee
    WHERE managerId IS NOT NULL
    GROUP BY managerId
    HAVING COUNT(*) >= 5
) M ON E.id = M.managerId;

-- Alternative 1
-- WITH managers AS (
--     SELECT managerId
--     FROM Employee
--     WHERE managerId IS NOT NULL
--     GROUP BY managerId
--     HAVING COUNT(*) >= 5
-- )
-- SELECT E.name
-- FROM Employee E
-- JOIN managers M ON E.id = M.managerId;

-- Alternative 2
-- SELECT name
-- FROM Employee
-- WHERE id IN (
--     SELECT managerId
--     FROM Employee
--     WHERE managerId IS NOT NULL
--     GROUP BY managerId
--     HAVING COUNT(*) >= 5
-- );