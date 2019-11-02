CREATE SCHEMA `member_db` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;

use member_db;

-- CREATE TABLE `student_db`.`management_table` (
--   `student_id` INT NOT NULL AUTO_INCREMENT,
--   `student_name` TEXT NULL,
--   `student_college` TEXT NULL,
--   `student_address` TEXT NULL,
--   `student_phone` TEXT NULL,
--   PRIMARY KEY (`student_id`)
-- );

CREATE TABLE IF NOT EXISTS `member` (
  mem_id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
  firstname TEXT,
  lastname TEXT,
  gender TEXT,
  address TEXT,
  username TEXT,
  password TEXT
);