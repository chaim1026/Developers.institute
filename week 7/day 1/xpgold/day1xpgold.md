CREATE TABLE student (
    id_num SERIAL PRIMARY KEY,
    last_name VARCHAR (100) NOT NULL,
    first_name VARCHAR (100) NOT NULL,
   	birth_date TIMESTAMP NOT NULL
);

INSERT INTO student (last_name, first_name, birth_date)
VALUES ('Mark', 'Dupont', '1998-11-02'),('Yoan', 'Durant', '2010-03-12'),('Lea', 'Martin','1987-07-24'),('Sarah', 'Benichou', '1996-04-07'),('lea', 'Dupont', '2003-06-14'),('Omer', 'Simpson', '1980-03-10');

select * from student

select (last_name),(first_name) from student

select (last_name),(first_name) from student where id_num = 2

select * from student where last_name = 'Mark' and first_name = 'Dupont'

select * from student where last_name = 'Mark' or first_name = 'Dupont'

select (last_name),(first_name) from student where last_name like '%a%'

select (last_name),(first_name) from student where last_name like 'A%'

select (last_name),(first_name) from student where last_name like '%a'

select (last_name),(first_name) from student where right(last_name, 2) like 'a_'

select (last_name),(first_name) from student where id_num = 1 or id_num = 3

select (last_name),(first_name),(birth_date) from student where birth_date >= '2000-01-01'