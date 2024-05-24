-- Display the top 3 cities' temperatures during July and August ordered by temperature (descending)
CREA TABLE IF NOT EXISTS temp_july_aug
SELECT *
FROM temperatures WHERE mont =7 OR month = 8;

SELECT city, AVG(temp) AS avg_temp
FROM temperatures
WHERE month IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
