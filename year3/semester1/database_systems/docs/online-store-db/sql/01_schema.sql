DROP SCHEMA IF EXISTS shop CASCADE;
CREATE SCHEMA shop;
SET search_path = shop;

-- ========== CUSTOMER ==========
CREATE TABLE customer (
  customer_id   SERIAL PRIMARY KEY,
  name          VARCHAR(100) NOT NULL,
  email         VARCHAR(120) UNIQUE NOT NULL,
  phone         VARCHAR(30),
  created_at    TIMESTAMP NOT NULL DEFAULT NOW()
);

-- ========== PRODUCT ==========
CREATE TABLE product (
  product_id    SERIAL PRIMARY KEY,
  name          VARCHAR(120) NOT NULL,
  price         NUMERIC(10,2) NOT NULL CHECK (price >= 0),
  category      VARCHAR(60),
  active        BOOLEAN NOT NULL DEFAULT TRUE
);

-- ========== ORDER ==========
CREATE TABLE "order" (
  order_id      SERIAL PRIMARY KEY,
  customer_id   INT NOT NULL REFERENCES customer(customer_id) ON DELETE RESTRICT,
  order_date    DATE NOT NULL DEFAULT CURRENT_DATE,
  status        VARCHAR(30) NOT NULL DEFAULT 'NEW',
  total_amount  NUMERIC(12,2) NOT NULL DEFAULT 0
);

-- ========== ORDER ITEM ==========
CREATE TABLE order_item (
  order_item_id SERIAL PRIMARY KEY,
  order_id      INT NOT NULL REFERENCES "order"(order_id) ON DELETE CASCADE,
  product_id    INT NOT NULL REFERENCES product(product_id) ON DELETE RESTRICT,
  qty           INT NOT NULL CHECK (qty > 0),
  unit_price    NUMERIC(10,2) NOT NULL CHECK (unit_price >= 0),
  line_total    NUMERIC(12,2) NOT NULL
);

ALTER TABLE order_item
  ADD CONSTRAINT order_item_line_total_chk
  CHECK (line_total = qty * unit_price);

-- ========== PAYMENT ==========
CREATE TABLE payment (
  payment_id   SERIAL PRIMARY KEY,
  order_id     INT NOT NULL REFERENCES "order"(order_id) ON DELETE CASCADE,
  method       VARCHAR(20) NOT NULL
               CHECK (method IN ('card','cash','transfer','paypal')),
  amount       NUMERIC(12,2) NOT NULL CHECK (amount >= 0),
  paid_at      TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE INDEX ix_payment_order_id
  ON payment(order_id);

-- ========== SHIPMENT ==========
CREATE TABLE shipment (
  shipment_id  SERIAL PRIMARY KEY,
  order_id     INT NOT NULL REFERENCES "order"(order_id) ON DELETE CASCADE,
  carrier      VARCHAR(40) NOT NULL,
  tracking_no  VARCHAR(60) UNIQUE,
  shipped_at   TIMESTAMP,
  delivered_at TIMESTAMP,
  status       VARCHAR(20) NOT NULL DEFAULT 'pending'
               CHECK (status IN ('pending','shipped','delivered','returned'))
);

CREATE INDEX ix_shipment_order_id
  ON shipment(order_id);

