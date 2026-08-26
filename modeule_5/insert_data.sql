INSERT INTO customers (name, email, phone, city)
VALUES 
  ('John Reed',    'john.reed@mail.com',     '01553453465', 'Dhaka'),
  ('Sarah Khan',   'sarah.khan@mail.com',    '01711223344', 'Chittagong'),
  ('Mike Thompson', 'mike.t@mail.com',       '01899887766', 'Dhaka'),
  ('Emily Chen',   'emily.chen@mail.com',    NULL,          'Sylhet'),
  ('David Roy',    'david.roy@mail.com',     '01655443322', 'Khulna');


INSERT INTO categories (category_name)
VALUES 
  ('Electronics'),
  ('Furniture'),
  ('Clothing'),
  ('Books'),
  ('Groceries');


INSERT INTO products (product_name, price, stock, category_id)
VALUES 
  ('Laptop Pro',        85000.00, 10, 1), 
  ('Wireless Headphones', 4500.00, 25, 1),
  ('Office Desk',       12000.00, 5,  2),
  ('Office Chair',      8500.00,  8,  2),
  ('Cotton T-Shirt',    1200.00,  50, 3),
  ('Jeans',             2500.00,  30, 3),
  ('Science Fiction Novel', 600.00, 30, 4),
  ('Cookbook',          750.00,  15, 4),
  ('Organic Rice (5kg)', 500.00,  40, 5),
  ('Olive Oil (1L)',    1200.00,  20, 5);


INSERT INTO orders (customer_id, order_date, total_amount)
VALUES 
  (1, '2026-08-20 10:15:00', 85000.00),   
  (2, '2026-08-21 14:30:00', 7000.00),   
  (1, '2026-08-22 09:00:00', 2500.00),
  (3, '2026-08-23 16:45:00', 12000.00),
  (4, '2026-08-24 11:20:00', 600.00),
  (5, '2026-08-24 13:50:00', 1950.00),
  (2, '2026-08-25 08:30:00', 8500.00),
  (3, '2026-08-26 12:00:00', 1700.00);