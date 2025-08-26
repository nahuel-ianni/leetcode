-- Solution to the 'Monthly Transactions I' problem.
-- Write your PostgreSQL query statement below.

SELECT
    TO_CHAR(T.trans_date, 'YYYY-MM') AS month,
    T.country,
    COUNT(*) AS trans_count,
    SUM(CASE WHEN T.state = 'approved' THEN 1 ELSE 0 END) AS approved_count,
    SUM(T.amount) AS trans_total_amount,
    SUM(CASE WHEN T.state = 'approved' THEN T.amount ELSE 0 END) AS approved_total_amount
FROM Transactions T
GROUP BY month, T.country;