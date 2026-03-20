-- q3_window_function.sql
SET search_path = shop;

SELECT
  c.customer_id,
  c.name                    AS customer_name,
  o.order_id,
  o.order_date,
  oi.order_item_id,
  p.name                    AS product_name,
  oi.line_total,
  COALESCE(pay.amount, 0)   AS payment_amount,
  ship.status               AS shipment_status,
  SUM(oi.line_total) OVER (
      PARTITION BY c.customer_id
      ORDER BY o.order_date, o.order_id, oi.order_item_id
      ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
  ) AS running_total_by_customer
FROM customer      AS c
JOIN "order"       AS o    ON o.customer_id = c.customer_id
JOIN order_item    AS oi   ON oi.order_id   = o.order_id
JOIN product       AS p    ON p.product_id  = oi.product_id
LEFT JOIN payment  AS pay  ON pay.order_id  = o.order_id
LEFT JOIN shipment AS ship ON ship.order_id = o.order_id
ORDER BY
  c.customer_id,
  o.order_date,
  o.order_id,
  oi.order_item_id;
