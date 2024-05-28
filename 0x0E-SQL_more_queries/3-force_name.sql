-- create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- switch to the database 
USE hbtn_0d_2;

-- create table force_name if not exists
CREATE TABLE IF NOT EXISTS force_name (
	id INT,
	name VARCHAR(256) NOT NULL
	);

-- Insert data into the table
INSERT INTO force_name (id, name) VALUES
(1, 'Holberton School'),
(1, 'Python is cool'),
(2, 'Holberton'),
(3, 'School'),
(4, 'C is fun');
