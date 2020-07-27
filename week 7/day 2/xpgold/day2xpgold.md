SELECT * FROM customer

SELECT (first_name, last_name) AS full_name FROM customer

SELECT DISTINCT create_date
FROM customer;

SELECT * FROM customer ORDER BY first_name DESC;

SELECT film_id, title, description, release_year, rental_rate FROM film ORDER BY rental_rate;

SELECT address, district, phone FROM address 
WHERE district = 'Texas';

SELECT * FROM film
WHERE film_id = 15 or film_id =150;

SELECT film_id, title, description, length, rental_rate FROM film 
WHERE title = 'The Wedding Ringer';

SELECT film_id, title, description, length, rental_rate FROM film 
WHERE title like 'Th%';

SELECT * FROM film ORDER BY rental_rate ASC LIMIT 10;

SELECT * FROM film ORDER BY rental_rate ASC OFFSET 10 LIMIT 10;

SELECT customer.customer_id, customer.last_name, payment.amount, payment.payment_date
FROM customer
INNER JOIN payment 
ON customer.customer_id = payment.customer_id;

SELECT customer.customer_id, customer.last_name, payment.amount, payment.payment_date, payment.staff_id
FROM customer
INNER JOIN payment
ON customer.customer_id = payment.customer_id
ORDER BY staff_id;

SELECT * FROM film 
WHERE film_id NOT IN (SELECT film_id FROM inventory);

SELECT country.country, city.city
FROM city
INNER JOIN country
ON city.country_id = country.country_id

ALTER TABLE film
ADD cheap_expensive VARCHAR (20);
UPDATE film 
SET cheap_expensive = 'cheap'
WHERE rental_rate < 2.00;
UPDATE film 
SET cheap_expensive = 'expensive'
WHERE rental_rate > 2.00;