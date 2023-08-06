'''The given SQL query uses a Common Table Expression (CTE) to create an intermediate result set named CTE, which contains all the columns from the world table. Then, it selects the name, population, and area columns from the CTE, filtering the results to include only rows where the area is greater than or equal to 3,000,000 or the population is greater than or equal to 25,000,000.
'''
WITH CTE AS (select * from world)
select name, population, area 
from CTE where area >= 3000000 or population >= 25000000;
