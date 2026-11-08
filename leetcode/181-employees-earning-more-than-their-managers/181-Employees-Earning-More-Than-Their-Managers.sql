select
    e.name as Employee
from Employee e
Join Employee m on e.managerId = m.id
where e.salary > m.salary