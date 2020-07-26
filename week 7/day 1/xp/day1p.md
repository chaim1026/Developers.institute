CREATE TABLE items  (
	id_num SERIAL PRIMARY KEY,
    product VARCHAR (100) NOT NULL,
    price SMALLINT NOT NULL
);

CREATE TABLE customers  (
	id_num SERIAL PRIMARY KEY,
    first_name VARCHAR (100) NOT NULL,
    last_name VARCHAR (100) NOT NULL
);

INSERT INTO items (product, price)
VALUES ('small_desk', 100),('large_desk', 300),('fan', 80);

INSERT INTO customers (first_name, last_name)
VALUES ('Greg', 'Jones'),('Sandra', 'Jones'),('Scott', 'Scott'),('Trevor', 'Green'),('Melanie', 'Johnson');

select * from items

select * from customers

select * from items where price > 80

select * from items where price < 30

select * from customers where last_name = 'Smith'

select * from customers where not first_name = 'Craig'