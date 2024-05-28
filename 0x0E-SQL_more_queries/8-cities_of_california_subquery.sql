-- use database hbtn_0d_usa
USE hbtn_0d_usa;
-- Select all rows from the cities table
SELECT * 
-- Filter the rows based on the state_id
FROM cities 
-- Use a subquery to find the id of the state with the name 'California'
WHERE state_id = (
    -- Subquery to get the id of the state 'California'
    SELECT id 
    -- From the states table
    FROM states 
    -- Where the name is 'California'
    WHERE name = 'California'
)
-- Order the results by city id
ORDER BY id;
