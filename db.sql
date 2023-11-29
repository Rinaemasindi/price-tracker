-- Create the saletracker database if it doesn't exist
CREATE DATABASE IF NOT EXISTS saletracker;

-- Use the saletracker database
USE saletracker;

-- Create the shop table
CREATE TABLE IF NOT EXISTS shop (
    shop_id INT AUTO_INCREMENT PRIMARY KEY,
    shop_name VARCHAR(255) NOT NULL
);

-- Create the producttype table
CREATE TABLE IF NOT EXISTS producttype (
    product_type_id INT AUTO_INCREMENT PRIMARY KEY,
    product_type VARCHAR(255) NOT NULL
);

-- Create the product table
CREATE TABLE IF NOT EXISTS product (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    product_price DECIMAL(10, 2) NOT NULL,
    product_image VARCHAR(255),
    product_url VARCHAR(255),
    shop_id INT NOT NULL,
    product_type_id INT,
    FOREIGN KEY (shop_id) REFERENCES shop(shop_id),
    FOREIGN KEY (product_type_id) REFERENCES producttype(product_type_id)
);

-- Insert shops into the shop table
INSERT INTO shop (shop_name) VALUES
('game'),
('hificorp'),
('evetech'),
('makro'),
('russells'),
('okfurniture'),
('takealot'),
('incredible');

-- Modify the product table to add a date column
ALTER TABLE product
ADD COLUMN created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP;

-- Modify the shop table to add a date column
ALTER TABLE shop
ADD COLUMN created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP;

-- Modify the producttype table to add a date column
ALTER TABLE producttype
ADD COLUMN created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP;

ALTER TABLE product
MODIFY COLUMN created_at DATE DEFAULT CURRENT_DATE;