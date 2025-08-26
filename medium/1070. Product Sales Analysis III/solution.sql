-- Solution to the 'Product Sales Analysis III' problem.
-- Write your PostgreSQL query statement below.

SELECT
    product_id,
    year as first_year,
    quantity,
    price
FROM Sales
WHERE (product_id, year) IN (
    SELECT product_id, min(year) AS year FROM Sales GROUP BY product_id
)