-- Creates the database 'hbtn_0d_usa'.
-- If database already exists, the script should not fail.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create the user 'states'.
-- Id INT unique, auto generated, can’t be null and is a primary key.
-- The name VARCHAR(256) can’t be null
-- If user already exists, script should not fail.
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, name VARCHAR(256) NOT NULL)

