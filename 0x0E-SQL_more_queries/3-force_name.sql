-- create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- switch to the database 
USE hbtn_0d_2;

-- create table force_name if not exists
CREATE TABLE IF NOT EXISTS force_name (
	id INT,
	name VARCHAR(256) NOT NULL
	);
