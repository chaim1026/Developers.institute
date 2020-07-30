UPDATE FILM
SET language_id = 2
WHERE film_id BETWEEN 272 AND 278;

INSERT INTO address (address, district, city_id, postal_code, phone, last_update)
VALUES ('23891 Wendover Dr', 'Bern', 72, 44122, 12162917768, '2020-07-28'),
('23995 Wendover Dr', 'Bern', 72, 44122, 12162937568, '2020-07-28'),
('44891 Greenlawn Ave', 'Bern', 72, 44122, 12162098768, '2020-07-28');

INSERT INTO customer (store_id, first_name, last_name, email, address_id, activebool, create_date, last_update, active) VALUES
(1, 'Tomer', 'Goldstein', 'tomer@gmail.com', 606, 'True', '2020-07-28', '2020-07-28', 1),
(2, 'Chaim', 'Wiesner', 'chaim@gmail.com', 607, 'True', '2020-07-28', '2020-07-28', 1),
(1, 'Jason', 'Kipp', 'jason@gmail.com', 608, 'True', '2020-07-28', '2020-07-28', 1)

same as exercise 2

that was in ninja did not do it yet but you cant delete it since it has foreign keys

SELECT film.description,film.title, actor.first_name, actor.last_name
FROM film
JOIN film_actor on film.film_id = film_actor.film_id
JOIN actor on film_actor.actor_id = actor.actor_id
WHERE actor.first_name = 'Penelope' AND actor.last_name = 'Monroe' AND film.description like '%Sumo%';

SELECT * FROM film
WHERE length < 60 AND rating = 'R' AND description like '%Documentary%';

SELECT customer.first_name, customer.last_name, payment.amount, rental.return_date, film.title
FROM customer
JOIN payment ON customer.customer_id = payment.customer_id
JOIN rental ON payment.rental_id = rental.rental_id
JOIN inventory ON rental.inventory_id = inventory.inventory_id
JOIN film ON inventory.film_id = film.film_id
WHERE customer.first_name = 'Matthew' AND customer.last_name = 'Mahan' AND payment.amount > 4.00 AND rental.return_date BETWEEN '2005-07-28' AND '2005-08-01';

(SELECT DISTINCT customer.first_name, customer.last_name, film.title, film.description
FROM customer
JOIN inventory ON customer.store_id = inventory.store_id
JOIN film ON inventory.film_id = film.film_id
WHERE customer.first_name = 'Matthew' AND customer.last_name = 'Mahan' AND (film.title like '%Boat%' or film.description like '%Boat%') AND film.replacement_cost = 29.99;

SELECT DISTINCT customer.first_name, customer.last_name, film.title, film.description, film.)replacement_cost
FROM film
JOIN inventory ON film.film_id = inventory.film_id
JOIN rental ON inventory.inventory_id = rental.inventory_id
JOIN customer ON rental.customer_id = customer.customer_id
WHERE customer.first_name = 'Matthew' AND customer.last_name = 'Mahan' 
AND (film.title like '%Boat%' or film.description like '%Boat%')
ORDER BY film.replacement_cost DESC LIMIT 1;

there are 9 possible movies

CREATE VIEW Joe_Swank_Action_Films AS
SELECT actor.first_name, actor.last_name, film.description
FROM actor
JOIN film_actor ON actor.actor_id = film_actor.actor_id
JOIN film ON film_actor.film_id = film.film_id
WHERE film.description like '%Action%' AND actor.first_name = 'Joe' AND actor.last_name = 'Swank';

INSERT INTO rental (rental_date, inventory_id, customer_id, return_date, staff_id, last_update)
VALUES ('2020-08-28', 37, 601, '2020-09-10', 2, '2020-08-28'),
('2020-08-28', 38, 601, '2020-09-10', 2, '2020-08-28'),
('2020-08-28', 39, 601, '2020-09-10', 2, '2020-08-28');

INSERT INTO payment (customer_id, staff_id, rental_id, amount, payment_date)
VALUES (601, 2, 16050, 4.99, '2020-08-28'),(601, 2, 16051, 4.99, '2020-08-28'),(601, 2, 16052, 4.99, '2020-08-28');

SELECT film.title, film.description
FROM film 
JOIN inventory ON film.film_id = inventory.film_id
JOIN rental ON inventory.inventory_id = rental.inventory_id
JOIN customer ON rental.customer_id = customer.customer_id
WHERE customer.customer_id = 601 AND inventory.inventory_id = 37;