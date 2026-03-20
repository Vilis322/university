-- q1_inner_or_left_join.sql
SET search_path = shop;

SELECT
  c.customer_id,
  c.name                AS customer_name,
  o.order_id,
  o.order_date,
  p.name                AS product_name,
  oi.qty,
  oi.unit_price,
  oi.line_total,
  pay.method            AS payment_method,
  pay.amount            AS payment_amount,
  ship.carrier,
  ship.status           AS shipment_status
FROM "order"      AS o
JOIN customer      AS c   ON c.customer_id = o.customer_id
JOIN order_item    AS oi  ON oi.order_id   = o.order_id
JOIN product       AS p   ON p.product_id  = oi.product_id
LEFT JOIN payment  AS pay ON pay.order_id  = o.order_id
LEFT JOIN shipment AS ship ON ship.order_id = o.order_id
ORDER BY
  o.order_id,
  oi.order_item_id;
