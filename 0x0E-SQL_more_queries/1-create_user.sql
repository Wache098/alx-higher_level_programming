-- Create the user user_0d_1 with the specified password
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- grant all privileges to the user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- flush the privileges to ensure that they are applied
FLUSH PRIVILEGES;
