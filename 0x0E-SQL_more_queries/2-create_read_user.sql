-- Creates the database hbtn_0d_2.
-- If database already exists, the script should not fail.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the user user_0d_2.
-- The user_0d_2 password should be set to user_0d_2_pwd.
-- If user already exists, script should not fail.
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- User should have only SELECT privilege in the database hbtn_0d_2.
GRANT SELECT ON hbtn_0d_2 * TO 'user_0d_2'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
