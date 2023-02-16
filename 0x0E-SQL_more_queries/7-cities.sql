-- Creates the database 'hbtn_0d_usa'.
-- If database already exists, the script should not fail.
-- Create the user 'cities'.
-- Id INT unique, auto generated, can’t be null and is a primary key.
-- The state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table
-- The name VARCHAR(256) can’t be null.
-- If user already exists, script should not fail.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, state_id INT NOT NULL, name VARCHAR(256) NOT NULL, FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id));

