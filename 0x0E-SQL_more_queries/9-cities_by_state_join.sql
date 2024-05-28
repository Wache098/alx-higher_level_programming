-- Selects the city ID, city name, and corresponding state name
SELECT cities.id, cities.name, states.name
-- Specifies the tables to retrieve data from
FROM cities
-- Joins the cities table with the states table based on the state_id foreign key relationship
JOIN states ON cities.state_id = states.id
-- Orders the result set in ascending order by city ID
ORDER BY cities.id ASC;
