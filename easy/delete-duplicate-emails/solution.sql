-- Solution to the 'Delete Dumplicate Emails' problem.
-- Write your PostgreSQL query statement below.

DELETE FROM Person a
USING Person b
WHERE a.id > b.id AND a.email = b.email;