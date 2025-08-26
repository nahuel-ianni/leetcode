-- Solution to the 'Immediate Food Delivery II' problem.
-- Write your PostgreSQL query statement below.

WITH cte AS (
    SELECT DISTINCT ON(customer_id) *
    FROM Delivery
    ORDER BY customer_id, order_date
)
SELECT ROUND(
    AVG((order_date = customer_pref_delivery_date)::INT) * 100,
    2
) AS immediate_percentage
FROM cte;

-- Alternative
-- SELECT ROUND(
--     AVG((order_date = customer_pref_delivery_date)::INT) * 100,
--     2
-- ) AS immediate_percentage
-- FROM (
--     SELECT *
--     FROM Delivery
--     WHERE order_date = (
--         SELECT MIN(order_date)
--         FROM Delivery d2
--         WHERE d2.customer_id = Delivery.customer_id
--     )
-- ) AS first_orders;