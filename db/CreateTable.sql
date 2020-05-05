CREATE DATABASE result;
USE result;
CREATE TABLE IF NOT EXISTS result
             (
                          id         INTEGER NOT NULL AUTO_INCREMENT,
                          result     VARCHAR(100) NOT NULL,
                          PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
