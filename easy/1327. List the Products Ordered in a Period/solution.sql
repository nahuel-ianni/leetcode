-- Solution for the 'List the Products Ordered in a Period' problem.
-- Write your PostgreSQL query statement below.

SELECT P.product_name, SUM(O.unit) AS unit
FROM Products P
JOIN Orders O ON P.product_id = O.product_id
WHERE EXTRACT(MONTH FROM O.order_date) = 2 AND
      EXTRACT(YEAR FROM O.order_date) = 2020
GROUP BY P.product_name
HAVING SUM(O.unit) >= 100