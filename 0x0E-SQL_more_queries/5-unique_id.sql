-- Creates the table unique_id on your MySQL serve.
-- The database name will be passed as an argument of the mysql command.
-- If the table unique_id already exists, your script should not fail
-- id INT default value 1  and must be unique, name VARCHAR(256)

CREATE TABLE IF NOT EXISTS unique_id (id INT UNIQUE DEFAULT 1, name VARCHAR(256));
