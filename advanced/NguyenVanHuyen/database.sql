CREATE SCHEMA `account_db` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;

use account_db;

CREATE TABLE IF NOT EXISTS `user` (
	id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
    username TEXT,
	firstname TEXT,
	lastname TEXT,
	gender TEXT,
	address TEXT
);