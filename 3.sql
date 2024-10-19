#3.	Write a SQL query to retrieve all books that have been ordered more than 10 times, along with the total quantity ordered for each book.

SELECT b.book_id, b.title, COUNT(DISTINCT od.order_id) AS total_orders, SUM(od.quantity) AS total_quantity
FROM Books b
JOIN OrderDetails od ON b.book_id = od.book_id
JOIN Orders o ON od.order_id = o.order_id
GROUP BY b.book_id, b.title
HAVING COUNT(DISTINCT od.order_id) > 10;
