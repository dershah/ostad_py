-- Show all customers.
SELECT*FROM customers

-- Show all products
SELECT*FROM products

-- Show products whose price is greater than 1000.
SELECT*FROM products
WHERE price>1000;

-- Show products whose stock is less than 10
SELECT*FROM products
WHERE stock<10;

-- Show customers from Dhaka
SELECT*FROM customers
WHERE city= 'Dhaka'

-- Sort products by price (Highest to Lowest)
SELECT*FROM products
ORDER BY price DESC; 

-- Sort customers alphabetically
SELECT * FROM customers ORDER BY name;
-- Show the first 5 products
SELECT * FROM products 
ORDER BY product_id 
LIMIT 5;

-- Count total customers
SELECT COUNT(*) AS total_customers
FROM customers;

-- Calculate the average product price
SELECT ROUND(AVG(price), 2) AS average_price 
FROM products;
