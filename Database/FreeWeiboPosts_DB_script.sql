USE FreeWeibo;

CREATE TABLE FreeWeiboPosts (
Post_Id INT NOT NULL AUTO_INCREMENT,
User_name VARCHAR(100),
FreeWeibo_Post_Id VARCHAR(20) NOT NULL UNIQUE,
repostscount MEDIUMINT,
censored TINYINT,
deleted TINYINT,
adult_keyword BOOLEAN,
censored_keyword BOOLEAN,
time_created DATETIME,
OriginalPostLink TINYTEXT,
HotTerm VARCHAR(255),
content TEXT,
time_scrapped DATETIME,
PRIMARY KEY(Post_Id)
)ENGINE = InnoDB;


CREATE USER 'admin'@'localhost' IDENTIFIED BY 'freeweibo2021';

GRANT ALL ON FreeWeibo.FreeWeiboPosts TO 'admin'@'localhost';

#Add Column Containing Weibo users ID to current table
ALTER TABLE FreeWeiboPosts
ADD COLUMN weibo_user_id VARCHAR(100) AFTER User_name;

ALTER TABLE `FreeWeibo`.`FreeWeiboPosts` 
ADD INDEX `index3` (`weibo_user_id` ASC) VISIBLE;
;

ALTER TABLE `FreeWeibo`.`FreeWeiboPosts` 
ADD INDEX `fk_freeweibo_hotterm_idx` (`HotTerm` ASC) VISIBLE;
;
ALTER TABLE `FreeWeibo`.`FreeWeiboPosts` 
ADD CONSTRAINT `fk_freeweibo_hotterm`
  FOREIGN KEY (`HotTerm`)
  REFERENCES `FreeWeibo`.`HOTTERMS` (`HotTerm`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;


