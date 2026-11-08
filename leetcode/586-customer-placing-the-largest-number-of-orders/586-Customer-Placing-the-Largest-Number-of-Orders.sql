select customer_number from Orders
group by customer_number
order by count(order_number) Desc
limit 1;