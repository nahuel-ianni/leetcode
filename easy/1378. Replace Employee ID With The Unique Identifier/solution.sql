-- Solution to the 'Replace Employee ID With The Unique Identifier' problem.
-- Write your PostgreSQL query statement below

SELECT EmployeeUNI.unique_id, Employees.name
FROM Employees
LEFT JOIN EmployeeUNI 
ON Employees.id = EmployeeUNI.id