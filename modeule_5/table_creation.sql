-- Customer Table
CREATE TABLE customers (
    customer_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    city VARCHAR(50) NOT NULL
);

-- Products Table
CREATE TABLE categories (
    category_id  INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL
);
-- Products Table
CREATE TABLE products (
    product_id  INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    product_name VARCHAR(50) NOT NULL,
    price NUMERIC(10,2),
    stock INT,
    category_id INT,
    Foreign Key (category_id) REFERENCES categories(category_id)
);
-- Orders Table
CREATE TABLE orders (
    order_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    customer_id INT,
    order_date TIMESTAMP,
    total_amount NUMERIC(10,2),
    Foreign Key (customer_id) REFERENCES customers(customer_id)
);
