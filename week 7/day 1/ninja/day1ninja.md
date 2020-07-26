select (last_name),(first_name) from student order by first_name asc limit 4

select (last_name),(first_name),(birth_date) from student order by birth_date desc limit 1

select (last_name),(first_name),(birth_date) from student offset 2 limit 3