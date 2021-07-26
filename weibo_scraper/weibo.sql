CREATE DATABASE Weibo;

USE Weibo;

CREATE TABLE WeiboPosts(
Post_Id INT NOT NULL AUTO_INCREMENT,
Content TEXT,
url TINYTEXT,
uid TINYTEXT,
pid TINYTEXT,
pubdate DATETIME,
tested TINYTEXT,
test_date TINYTEXT,
time_created DATETIME,
status TINYTEXT,
PRIMARY KEY(Post_Id),
)ENGINE = InnoDB;


CREATE USER 'admin'@'localhost' IDENTIFIED BY 'freeweibo2021';

GRANT ALL ON Weibo.WeiboPosts TO 'admin'@'localhost';
