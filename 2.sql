#2.	Write a SQL query to calculate the total revenue generated from book sales by each author.

SELECT b.author, SUM(od.quantity * b.price) AS total_revenue
FROM Books b
JOIN OrderDetails od ON b.book_id = od.book_id
JOIN Orders o ON od.order_id = o.order_id
GROUP BY b.author
ORDER BY total_revenue DESC;
