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

INSERT INTO `account_db`.`user` (`username`, `firstname`, `lastname`, `gender`, `address`) VALUES ('huyennv', 'Nguyễn ', 'Văn Huyện', 'nam', 'Quận 2');
INSERT INTO `account_db`.`user` (`username`, `firstname`, `lastname`, `gender`, `address`) VALUES ('hienth', 'Trần', 'Thanh Hiền', 'nữ', 'Quận 3');
INSERT INTO `account_db`.`user` (`username`, `firstname`, `lastname`, `gender`, `address`) VALUES ('thanh', 'Vũ', 'Văn Thanh', 'nam', 'Quận 1');