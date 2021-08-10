CREATE DATABASE FreeWeibo;

USE FreeWeibo;

CREATE TABLE FreeWeiboPosts (
Post_Id INT NOT NULL AUTO_INCREMENT,
User_name VARCHAR(50),
FreeWeibo_Post_Id VARCHAR(20) NOT NULL UNIQUE,
repostscount MEDIUMINT,
censored TINYINT,
deleted TINYINT,
adult_keyword BOOLEAN,
consored_keyword BOOLEAN,
time_created DATETIME,
OriginalPostLink TINYTEXT,
HotTerm VARCHAR(255),
content TEXT,
time_scrapped DATETIME,
PRIMARY KEY(Post_Id)#,
#CONSTRAINT fk_HotTerm FOREIGN KEY (HotTerm)
#REFERENCES FreeWeiboHotSearch(Term)
)ENGINE = InnoDB;

CREATE USER 'admin'@'localhost' IDENTIFIED BY 'freeweibo2021';

GRANT ALL ON FreeWeibo.FreeWeiboPosts TO 'admin'@'localhost';

#Add Column Containing Weibo users ID to current table
ALTER TABLE FreeWeiboPosts
ADD COLUMN weibo_id_user VARCHAR(100) AFTER User_name;

ALTER TABLE `FreeWeibo`.`FreeWeiboPosts` 
ADD INDEX `weibo_user` (`weibo_id_user` ASC) VISIBLE;

