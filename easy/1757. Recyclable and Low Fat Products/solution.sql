-- Solution to the 'Recyclable and Low Fat Products' problem

SELECT product_id
FROM Products
WHERE low_fats = 'Y' AND recyclable = 'Y';