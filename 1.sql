#1.	Write a SQL query to retrieve the top 5 customers who have purchased the most books (by total quantity) over the last year.
SELECT c.customer_id, c.name, SUM(od.quantity) AS total_books
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
JOIN OrderDetails od ON o.order_id = od.order_id
WHERE o.order_date >= DATE_SUB(CURDATE(), INTERVAL 2 YEAR)
GROUP BY c.customer_id, c.name
ORDER BY total_books DESC
LIMIT 5;


