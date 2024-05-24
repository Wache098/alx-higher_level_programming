-- Import the provided table dump into the hbtn_0c_0 database
-- (Assuming the table dump file is named temperatures_table_dump.sql)
SELECT city, AVG(value) AS avg_temp
FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
