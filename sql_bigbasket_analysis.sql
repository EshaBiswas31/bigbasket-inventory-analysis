-- Create database
CREATE DATABASE ecommerce_inventory;
USE ecommerce_inventory;

-- Create table
CREATE TABLE bigbasket_products_new (
    product_name VARCHAR(255),
    category VARCHAR(100),
    sub_category VARCHAR(100),
    brand VARCHAR(100),
    sale_price FLOAT,
    market_price FLOAT,
    rating FLOAT,
    price_bucket VARCHAR(20),
    demand_score VARCHAR(20)
);

-- Check nulls
SELECT * FROM bigbasket_products_new
WHERE rating IS NULL;

-- Remove duplicates example
SELECT product_name, COUNT(*)
FROM bigbasket_products_new
GROUP BY product_name
HAVING COUNT(*) > 1;

-- Create price bucket
UPDATE bigbasket_products_new
SET price_bucket =
CASE
    WHEN sale_price < 100 THEN 'Low'
    WHEN sale_price BETWEEN 100 AND 300 THEN 'Medium'
    ELSE 'High'
END;

-- Category distribution
SELECT category, COUNT(*) AS total_products
FROM bigbasket_products_new
GROUP BY category
ORDER BY total_products DESC;

-- Demand distribution
SELECT demand_score, COUNT(*)
FROM bigbasket_products_new
GROUP BY demand_score;

-- Category vs price bucket
SELECT category, price_bucket, COUNT(*)
FROM bigbasket_products_new
GROUP BY category, price_bucket;

