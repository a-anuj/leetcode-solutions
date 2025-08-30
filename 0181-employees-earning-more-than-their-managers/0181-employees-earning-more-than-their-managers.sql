# Write your MySQL query statement below
SELECT e.name as Employee from Employee e WHERE e.salary > (select m.salary from Employee m where m.id=e.managerId)