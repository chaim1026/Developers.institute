exercise 1

UPDATE student
SET first_name = 'Lea'
WHERE first_name = 'lea';

UPDATE student
SET birth_date = '1998-11-02'
WHERE last_name = 'Dupont';

DELETE FROM student WHERE first_name = 'Lea' and last_name =  'Dupont';

select count(*) as num_of_students from student

select count(*) as num_of_students from student
where birth_date > '2000-01-01'

ALTER TABLE student
ADD math_grade SMALLINT NOT NULL DEFAULT 0;

UPDATE student
SET math_grade = 80
WHERE id_num = 1;

UPDATE student
SET math_grade = 90
WHERE id_num = 2 or id_num = 4;

UPDATE student
SET math_grade = 100
WHERE id_num = 6;

SELECT COUNT(*) from student
WHERE math_grade > 83;

INSERT INTO student (first_name, last_name, birth_date, math_grade)
VALUES ((SELECT first_name from student WHERE id_num = 6),(SELECT last_name from student WHERE id_num = 6),(SELECT birth_date from student WHERE id_num = 6),(70));

SELECT first_name, last_name, COUNT(math_grade) as total_grades
FROM student
GROUP BY first_name,last_name;

SELECT SUM(math_grade) FROM student

exercise 2

select * from items ORDER BY price ASC

SELECT * FROM items 
WHERE price > 80
ORDER BY price DESC

SELECT first_name, last_name FROM customers ORDER BY first_name ASC LIMIT 3

SELECT first_name, last_name FROM customers ORDER BY first_name DESC LIMIT 2

SELECT last_name FROM customers ORDER BY last_name DESC 

does not work missing a field

INSERT INTO purchases (customer_id, item_id)
VALUES ((SELECT id_num from customers WHERE id_num = 1),1),
((SELECT id_num from customers WHERE id_num = 2),3),
((SELECT id_num from customers WHERE id_num = 3),3),
((SELECT id_num from customers WHERE id_num = 4),1),
((SELECT id_num from customers WHERE id_num = 5),2);

select * from purchases this is usefull now I know what all customers bought

SELECT item_id, customers.* 
FROM purchases
INNER JOIN customers
ON purchases.customer_id = customers.id_num;

SELECT item_id, customers.* 
FROM purchases
INNER JOIN customers
ON purchases.customer_id = customers.id_num
WHERE customers.id_num = 4;

SELECT item_id, customers.* 
FROM purchases
INNER JOIN customers
ON purchases.customer_id = customers.id_num
WHERE purchases.item_id = 1 or purchases.item_id = 2;

INSERT INTO items (product, price)
VALUES ('hard_drive', 50);
INSERT INTO purchases (customer_id, item_id)
VALUES ((SELECT id_num from customers WHERE first_name= 'Scott' and last_name = 'Scott'),(SELECT id_num FROM items WHERE product = 'hard_drive'))

DELETE FROM customers WHERE first_name ='Scott' and last_name = 'Scott';
cant delete while it is linked

SELECT customers.first_name, customers.last_name, items.product
FROM purchases
INNER JOIN customers ON purchases.customer_id = customers.id_num
INNER JOIN items ON purchases.item_id = items.id_num;