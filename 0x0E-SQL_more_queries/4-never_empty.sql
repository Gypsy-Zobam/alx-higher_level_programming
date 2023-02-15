-- Creates the table id_not_nul on your MySQL serve.
-- The database name will be passed as an argument of the mysql command.
-- If the table id_not_nul already exists, your script should not fail
-- id INT default value 1, name VARCHAR(256)
CREATE TABLE IF NOT EXISTS id_not_nul (id INT DEFAULT 1, name VARCHAR(256));
