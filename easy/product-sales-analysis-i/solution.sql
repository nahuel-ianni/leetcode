-- Solution to the 'Product Sales Analysis I' problem.
-- Write your PostgreSQL query statement below.

SELECT p.product_name, s.year, s.price
FROM Product p
JOIN Sales s
ON s.product_id = p.product_id