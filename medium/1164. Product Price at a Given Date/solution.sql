-- Solution to the 'Product Price at a Given Date' problem.
-- Write your PostgreSQL query statement below.

SELECT DISTINCT product_id,
       COALESCE(
           (SELECT new_price
            FROM Products p2
            WHERE p2.product_id = p1.product_id
            AND p2.change_date <= '2019-08-16'
            ORDER BY change_date DESC
            LIMIT 1),
           10
       ) as price
FROM Products p1
ORDER BY product_id