-- q2_aggregate_grouping.sql
SET search_path = shop;

SELECT
  c.customer_id,
  c.name                           AS customer_name,
  o.order_id,
  COUNT(oi.order_item_id)          AS items_in_order,
  SUM(oi.qty)                      AS total_qty,
  SUM(oi.line_total)               AS order_amount,
  COALESCE(SUM(DISTINCT pay.amount), 0) AS total_paid,
  COUNT(DISTINCT ship.shipment_id) AS shipments_count
FROM customer      AS c
JOIN "order"       AS o    ON o.customer_id = c.customer_id
JOIN order_item    AS oi   ON oi.order_id   = o.order_id
JOIN product       AS p    ON p.product_id  = oi.product_id
LEFT JOIN payment  AS pay  ON pay.order_id  = o.order_id
LEFT JOIN shipment AS ship ON ship.order_id = o.order_id
GROUP BY
  c.customer_id,
  c.name,
  o.order_id
ORDER BY
  c.customer_id,
  o.order_id;
