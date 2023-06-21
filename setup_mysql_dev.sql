-- This script prepares a MySQL server
-- A database hbnb_dev_db
-- A new user hbnb_dev (in localhost) with all privileges on the database hbnb_dev_db
-- hbnb_dev should have SELECT privilege on the database performance_schema

CREATE DATABASE IF NOT EXISTS hdnd_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
