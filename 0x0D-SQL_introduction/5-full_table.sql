-- Prints the full description of the table first_table from the database hbtn_0c_0
-- Prints the full description of the table first_table from the database hbtn_0c_0
SELECT COLUMN_NAME, COLUMN_TYPE
FROM information_schema.COLUMNS
WHERE TABLE_SCHEMA = 'hbtn_0c_0' AND TABLE_NAME = 'first_table';

