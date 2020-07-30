SELECT first_name AS "FIRST NAME", last_name AS "LAST NAME" FROM employees;
SELECT * FROM employees WHERE department_id = 2
SELECT * FROM employees ORDER BY first_name ASC
SELECT first_name, last_name, salary FROM employees
SELECT employee_id, (first_name,last_name) AS name, salary FROM employees ORDER BY salary ASC
SELECT SUM(salary) FROM employees
SELECT MIN(salary), MAX(salary) FROM employees
SELECT COUNT(employee_id), ROUND(AVG(salary),2) FROM employees
SELECT COUNT(employee_id) FROM employees
SELECT COUNT(DISTINCT job_id) FROM employees
SELECT UPPER(first_name) FROM employees
SELECT LEFT(first_name, 3) FROM employees
SELECT 171*214+625
SELECT (first_name,last_name) AS "NAME" FROM employees
SELECT TRIM(first_name) FROM employees
SELECT first_name, last_name, LENGTH(first_name) + LENGTH(last_name) FROM employees
SELECT first_name FROM employees WHERE first_name like '%[^0-9]%'
SELECT * FROM employees LIMIT 10
SELECT ROUND(salary / 12,2) FROM employees 

CREATE TABLE dup_countries (
 country_id SERIAL,
 country_name VARCHAR(100),
 region_id INTEGER,
 PRIMARY KEY (country_id)
);

CREATE TABLE countries (
 country_id SERIAL,
 country_name VARCHAR(100),
 region_id INTEGER,
 PRIMARY KEY (country_id)
 FOREIGN KEY (region_id) REFERENCES regions (region_id)
);

CREATE TABLE dup_countries (
 country_id SERIAL,
 country_name VARCHAR(100),
 region_id INTEGER,
 PRIMARY KEY (country_id)
 FOREIGN KEY (region_id) REFERENCES regions (region_id)
);

SELECT * INTO dup_countries FROM countries;

 CREATE TABLE countries (
   country_id SERIAL,
   country_name VARCHAR(100),
   region_id INTEGER NULL,
   PRIMARY KEY (country_id)
   FOREIGN KEY (region_id) REFERENCES regions (region_id)
 );

 CREATE TABLE jobs (
   job_id SERIAL,
   job_title VARCHAR(100),
   min_salary INTEGER,
   max_salary INTEGER,
   PRIMARY KEY (job_id),
   CHECK (max_salary >= 25000)
 );

 CREATE TABLE countries (
   country_id SERIAL,
   country_name VARCHAR(100),
   region_id INTEGER,
   PRIMARY KEY (job_id),
   FOREIGN KEY (region_id) REFERENCES (regions) (region_id)
   CHECK (country_name != 'Italy' OR country_name != 'India' OR country_name != 'China')
 );

 use serial and distinct

 CREATE TABLE jobs (
   job_id SERIAL,
   job_title VARCHAR(100),
   min_salary INTEGER DEFAULT 8000,
   max_salary INTEGER NULL,
   PRIMARY KEY (job_id),
 );

 serial primary key (country_id)

serial distinct

add distinct constraint

CREATE TABLE jobs_history (
   employee_id INTEGER DISTINCT,
   start_date DATE,
   end_date DATE,
   job_id INTEGER,
   FOREIGN KEY (employee_id) REFERENCES (employees) (employee_id),
   FOREIGN KEY (job_id) REFERENCES (jobs) (job_id)
 );

 use didtinct and unique constraint

 part 3

 SELECT (first_name, last_name), salary FROM employees WHERE salary NOT BETWEEN 10000 AND 15000;

SELECT (first_name, last_name), department_id  FROM employees
WHERE department_id = 30 OR department_id = 100
ORDER BY department_id ASC;

SELECT (first_name, last_name), department_id  FROM employees
WHERE department_id = 30 OR department_id = 100 AND salary NOT BETWEEN 10000 AND 15000 
ORDER BY department_id ASC;

SELECT (first_name, last_name), hire_date FROM employees
WHERE hire_date = '1987-01-01';

SELECT first_name FROM employees
WHERE first_name LIKE '%c%' AND first_name LIKE '%e%';

SELECT employees.last_name, jobs.job_title, employees.salary
FROM employees 
JOIN jobs ON employees.job_id = jobs.job_id
WHERE jobs.job_title != 'Programmer' OR jobs.job_title != 'Shipping Clerk'
AND employees.salary != 4500 AND employees.salary != 10000 AND employees.salary != 15000;

SELECT last_name FROM employees
WHERE last_name like '______'

SELECT last_name FROM employees
WHERE last_name like '__e%'

SELECT DISTINCT job_title FROM jobs

SELECT * FROM employees
WHERE last_name = 'Jones' OR last_name = 'Blake' OR last_name = 'King' OR last_name = 'Ford';