-- Lists all records of the table second_table of the database hbtn_0c_0, excluding rows without a name value and ordered by descending score
SELECT score, name FROM hbtn_0c_0.second_table WHERE name IS NOT NULL ORDER BY score DESC;
