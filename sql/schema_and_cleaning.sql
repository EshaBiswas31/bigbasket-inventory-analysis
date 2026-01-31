USE ecommerce_inventory;

-- Create cleaned working table
CREATE TABLE bigbasket_products_new AS
SELECT *
FROM `bigbasket products`;

-- Add price bucket
ALTER TABLE bigbasket_products_new
ADD COLUMN price_bucket VARCHAR(20);

UPDATE bigbasket_products_new
SET price_bucket =
CASE
    WHEN sale_price < 100 THEN 'Low'
    WHEN sale_price BETWEEN 100 AND 300 THEN 'Medium'
    ELSE 'High'
END;

-- Add demand score
ALTER TABLE bigbasket_products_new
ADD COLUMN demand_score VARCHAR(20);

UPDATE bigbasket_products_new
SET demand_score =
CASE
    WHEN rating >= 4 THEN 'High'
    WHEN rating BETWEEN 3 AND 3.9 THEN 'Medium'
    ELSE 'Low'
END;
