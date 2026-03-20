SET search_path = shop;

-- ========== CUSTOMERS ==========
INSERT INTO customer (name, email, phone) VALUES
('Anna Kovalskaia', 'anna@example.com', '+372-555-0101'),
('John Harris',     'jharris@example.com', '+1-555-2000'),
('Maria Gomez',     'maria@example.com',  '+34-600-110');

-- ========== PRODUCTS ==========
INSERT INTO product (name, price, category) VALUES
('Wireless Mouse',        19.99, 'Peripherals'),
('Mechanical Keyboard',   89.90, 'Peripherals'),
('USB-C Hub',             39.50, 'Accessories'),
('27"" Monitor',         239.00, 'Displays');

-- ========== ORDERS ==========
INSERT INTO "order" (customer_id, order_date, status, total_amount) VALUES
(1, CURRENT_DATE - 7, 'PAID', 0),
(1, CURRENT_DATE - 2, 'NEW',  0),
(2, CURRENT_DATE - 1, 'PAID', 0);

-- ========== ORDER ITEMS ==========
INSERT INTO order_item (order_id, product_id, qty, unit_price, line_total) VALUES
(1, 1, 2, 19.99, 2*19.99),
(1, 3, 1, 39.50, 1*39.50),
(2, 2, 1, 89.90, 1*89.90),
(3, 4, 2, 239.00, 2*239.00);

-- recalculate the order amount by items
UPDATE "order" o
SET total_amount = s.sum_total
FROM (
  SELECT order_id, SUM(line_total) AS sum_total
  FROM order_item
  GROUP BY order_id
) s
WHERE o.order_id = s.order_id;

-- ========== PAYMENTS ==========
INSERT INTO payment (order_id, method, amount, paid_at) VALUES
(1, 'card',     79.48, NOW() - INTERVAL '2 days'),
(2, 'transfer', 89.90, NOW() - INTERVAL '1 day'),
(3, 'paypal',  478.00, NOW() - INTERVAL '3 hours');

-- ========== SHIPMENTS ==========
INSERT INTO shipment (order_id, carrier, tracking_no, shipped_at, delivered_at, status) VALUES
(1, 'DHL', 'DHL123', NOW() - INTERVAL '6 days', NOW() - INTERVAL '5 days', 'delivered'),
(2, 'UPS', 'UPS456', NOW() - INTERVAL '1 day',  NULL,                     'shipped'),
(3, 'DHL', 'DHL789', NOW() - INTERVAL '4 hours', NULL,                    'shipped');

