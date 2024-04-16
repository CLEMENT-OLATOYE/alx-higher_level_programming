-- Create states table in hbtn-0e-0-usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e-0-usa;
USE hbtn-0e-0-usa;
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");