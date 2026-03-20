# Data Dictionary - Online Store (schema: shop)

## Table: customer
| Attribute   | Data Type    | Key | Description                                     |
|-------------|--------------|-----|-------------------------------------------------|
| customer_id | SERIAL       | PK  | Unique identifier of the customer.              |
| name        | VARCHAR(100) |     | Full name of the customer.                      |   
| email       | VARCHAR(120) | UQ  | Customers's email (must be unique).             |    
| phone       | VARCHAR(30)  |     | Contact phone number.                           |   
| created_at  | TIMESTAMP    |     | The timestamp when the customer was registered. |   


## Table: product
| Attribute  | Data Type     | Key | Description                               |
|------------|---------------|-----|-------------------------------------------|
| product_id | SERIAL        | PK  | Unique identifier of the product.         |
| name       | VARCHAR(120)  |     | Name of the product.                      |
| price      | NUMERIC(10,2) |     | Unit price. Must be non-negative.         |
| category   | VARCHAR(60)   |     | Category of the product.                  |
| active     | BOOLEAN       |     | Whether the product is active in catalog. |

## Table: order
| Attribute    | Data Type     | Key                        | Description                            |
|--------------|---------------|----------------------------|----------------------------------------|
| order_id     | SERIAL        | PK                         | Unique identifier of the order.        |
| customer_id  | INT           | FK -> customer.customer_id | Customer who placed the order.         |
| order_date   | DATE          |                            | Date when the order was created.       |
| status       | VARCHAR(30)   |                            | Status of the order (e.g., NEW, PAID). |
| total_amount | NUMERIC(12,2) |                            | Total monetary amount of the order.    |

## Table: order_item
| Attribute     | Data Type     | Key                      | Description                                             |
|---------------|---------------|--------------------------|---------------------------------------------------------|
| order_item_id | SERIAL        | PK                       | Unique identifier of the order item.                    |
| order_id      | INT           | FK -> order.order_id     | Order to which the item belongs.                        |
| product_id    | INT           | FK -> product.product_id | Purchased product.                                      |
| qty           | INT           |                          | Quantity of product in this order item. Must be > 0.    |
| unit_price    | NUMERIC(10,2) |                          | Price per unit at the moment of purchase.               |
| line_total    | NUMERIC(12,2) |                          | Total = qty * unit_price. Enforced by CHECK constraint. |

## Table: payment
| Attribute  | Data Type     | Key                  | Description                                        |
|------------|---------------|----------------------|----------------------------------------------------|
| payment_id | SERIAL        | PK                   | Unique identifier of the payment.                  |
| order_id   | INT           | FK -> order.order_id | Order that the payment covers.                     |
| method     | VARCHAR(20)   |                      | Payment method (card, cash, transfer, paypal etc.) |
| amount     | NUMERIC(12,2) |                      | Paid amount. Must be >= 0.                         |
| paid_at    | TIMESTAMP     |                      | Timestamp of payment. Defaults to NOW().           |

## Table: shipment
| Attribute    | Data Type   | Key                  | Description                                              |
|--------------|-------------|----------------------|----------------------------------------------------------|
| shipment_id  | SERIAL      | PK                   | Unique identifier of the shipment.                       |
| order_id     | INT         | FK -> order.order_id | Order being shipped.                                     |
| carrier      | VARCHAR(40) |                      | Shipping company (e.g. DHL, UPS).                        |
| tracking_no  | VARCHAR(60) | UQ                   | Tracking number. May be NULL initially.                  |
| shipped_at   | TIMESTAMP   |                      | Date/time when shipment was handed to carrier.           |
| delivered_at | TIMESTAMP   |                      | Date/time when shipment was delivered.                   |
| status       | VARCHAR(20) |                      | Shipment status (pending, shipped, delivered, returned). |
