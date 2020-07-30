CREATE TABLE items (
 id serial,
 name VARCHAR(50),
 price SMALLINT,
 PRIMARY KEY (id)
);

CREATE TABLE orders (
 id SERIAL,
 item_id INTEGER,
 customer_name VARCHAR(100)
 PRIMARY KEY (id),	
);

INSERT INTO items (name, price)
VALUES ('table', 70),('chair', 30),('cabinet', 80),('dresser', 60);

INSERT INTO orders (item_id)
VALUES (2),(1),(3),(2),(4),(3);

SELECT full_order.order_id, items.id, items.price FROM items
JOIN full_order ON items.id = full_order.item_id

CREATE TABLE full_order (
 item_id INTEGER,
 order_id INTEGER,
 FOREIGN KEY (item_id) REFERENCES items (id),
 FOREIGN KEY (order_id) REFERENCES orders (id)	
);

INSERT INTO full_order (item_id,order_id)
VALUES (1,2),(1,3),(2,1),(2,4),(2,2),(3,4),(4,1),(4,2),(4,5),(1,5),(3,6);


SELECT SUM(items.price)
FROM orders
JOIN full_order ON orders.id = full_order.order_id
JOIN items ON full_order.item_id = items.id
WHERE orders.id = 2;