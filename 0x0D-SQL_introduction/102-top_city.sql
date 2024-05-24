-- Display the top 3 cities' temperatures during July and August ordered by temperature (descending)
CREA TABLE IF NOT EXISTS temp_july_aug
SELECT *
FROM temperatures WHERE month =7 OR month = 8;

SELECT city, AVG(temp) AS avg_temp
FROM temp_july_aug
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
