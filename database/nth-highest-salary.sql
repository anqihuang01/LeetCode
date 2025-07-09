CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  Declare offset_val INT;
  set offset_val = N-1;

  RETURN (
      # Write your MySQL query statement below.
    select distinct Salary from Employee
    as getNthHighestSalary

    order by Salary Desc
    Limit 1 Offset offset_val
  );
END