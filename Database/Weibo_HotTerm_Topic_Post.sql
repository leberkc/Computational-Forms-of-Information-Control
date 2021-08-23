USE FreeWeibo;

CREATE TABLE Weibo_HotTerm_Topic_Post (
hotterm VARCHAR(255),
post_id VARCHAR(50),
mid VARCHAR(50),
created_at VARCHAR(50),
content TEXT,
textLength INT,
source TEXT,
favorited BOOLEAN,
weibo_user_id VARCHAR(20),
reposts_count INT,
comments_count INT,
attitudes_count INT,
time_scrapped DATETIME,
PRIMARY KEY(post_id)
)ENGINE = InnoDB

ALTER TABLE `FreeWeibo`.`Weibo_HotTerm_Topic_Post` 
CHANGE COLUMN `weibo_user_id` `weibo_user_id` VARCHAR(20) NOT NULL,
ADD INDEX `index2` (`weibo_user_id` ASC) VISIBLE;
;

ALTER TABLE `FreeWeibo`.`Weibo_HotTerm_Topic_Post` 
ADD INDEX `fk_weibo_hotterm_idx` (`hotterm` ASC) VISIBLE;
;
ALTER TABLE `FreeWeibo`.`Weibo_HotTerm_Topic_Post` 
ADD CONSTRAINT `fk_weibo_hotterm`
  FOREIGN KEY (`hotterm`)
  REFERENCES `FreeWeibo`.`HOTTERMS` (`HotTerm`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
  
GRANT ALL ON FreeWeibo.Weibo_HotTerm_Topic_Post TO 'admin'@'localhost';
