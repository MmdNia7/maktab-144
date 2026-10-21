--part 1

--1
--SELECT title , genre
--FROM books  
--WHERE genre = 'Fantasy'

--2
-- select customer_id , first_name , city
-- from customers
-- where city = 'Tehran'

--3
-- SELECT title , genre 
-- FROM books
-- WHERE genre = 'Romance' or genre = 'Novel'
-- WHERE genre IN ('Romance','Novel')
-- WHERE genre NOT IN ('Romance','Novel')

--4
-- SELECT title , price , stock , genre    
-- FROM books
-- WHERE price BETWEEN 10 AND 15 AND stock > 0 AND genre != 'Romance'

--5
-- SELECT first_name , email 
-- FROM customers
-- where first_name like 'S%' and email like '%.org'

--6
-- SELECT customer_id , first_name , last_name , city
-- from customers
-- WHERE city IS NULL

--7
-- SELECT title 
-- FROM books
-- WHERE title ILIKE '%love%'
-- WHERE title ~* 'love'
-- WHERE LOWER(title) LIKE '%love%'

--___________________________________________

--part 2


--1
-- SELECT first_name || ' ' || last_name AS full_name
-- from customers 

--2
-- SELECT min(price) as cheapest , MAX(price) as most_expensive
-- from books

--3
-- SELECT sum(quantity) as sum_quantity , ROUND(avg(quantity)::NUMERIC,2) as avg_quantity
-- from order_items

--4
-- SELECT title,price,pages, price::numeric / pages AS price_per_page
-- FROM books
-- ORDER BY price_per_page DESC
-- LIMIT 3; 

--5
-- SELECT title , price    
-- from books
-- WHERE price > (SELECT avg(price) FROM books)

--6
-- SELECT title , pages 
-- FROM books
-- WHERE pages = (SELECT max(pages) FROM books)

--7
-- SELECT customer_id,first_name, last_name
-- FROM customers
-- WHERE customer_id NOT IN (
--     SELECT customer_id
--     FROM orders
-- );

--______________________________________________

--part 3

-- --1
-- SELECT genre, COUNT(*) AS count_book
-- FROM books
-- GROUP BY genre
-- ORDER BY count_book DESC;

--2
-- SELECT author_id , count(*) as count_book 
-- from books
-- GROUP BY author_id

--3
-- SELECT status, count(*) as count_status
-- from orders
-- GROUP BY status

--4
-- SELECT genre, avg(price) as average_price
-- FROM books
-- GROUP BY genre
-- HAVING avg(price) > 13
-- ORDER BY average_price DESC

--5
-- SELECT order_id, sum(quantity * unit_price) as total_amount
-- from order_items
-- GROUP BY order_id
-- HAVING sum(quantity * unit_price) > 30

--6
--WHERE ردیف‌ها رو قبل از گروه‌بندی فیلتر می‌کنه.
--گروه‌ها رو بعد از گروه‌بندی و محاسبه‌ی توابع تجمیعی فیلتر میکند

-- SELECT order_id, SUM(quantity) AS total_quantity
-- FROM order_items
-- WHERE quantity > 2
-- GROUP BY order_id;

-- SELECT order_id, SUM(quantity) AS total_quantity
-- FROM order_items
-- GROUP BY order_id
-- HAVING SUM(quantity) > 2;


