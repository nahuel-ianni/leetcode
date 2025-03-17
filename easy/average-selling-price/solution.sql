-- Solution to the 'Average Selling Price' problem.
-- Write your PostgreSQL query statement below.

SELECT
    P.product_id,
    COALESCE(
        ROUND(SUM(s.units * p.price) / SUM(s.units)::NUMERIC, 2),
        0
    ) AS average_price
FROM Prices P
LEFT JOIN UnitsSold S
    ON P.product_id = S.product_id
    AND S.purchase_date BETWEEN P.start_date AND P.end_date
GROUP BY P.product_id