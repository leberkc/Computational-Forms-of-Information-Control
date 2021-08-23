USE FreeWeibo;

CREATE TABLE Weibo_User_data (
weibo_user_id VARCHAR(20),
screen_name VARCHAR(100),
profile_url TINYTEXT,
statuses_count INT,
verified BOOLEAN,
verified_type INT,
verified_reason TEXT,
close_blue_v BOOLEAN,
u_description TEXT,
gender char,
mbtype INT,
urank INT,
mbrank INT,
follow_me BOOLEAN,
following BOOLEAN,
followers_count INT,
follow_count INT,
origin VARCHAR(10),
time_scrapped DATETIME,
PRIMARY KEY(weibo_user_id, screen_name)
)ENGINE = InnoDB

ALTER TABLE `FreeWeibo`.`Weibo_User_data` 
ADD CONSTRAINT `fk_weibo_user`
  FOREIGN KEY (`weibo_user_id`)
  REFERENCES `FreeWeibo`.`Weibo_HotTerm_Topic_Post` (`weibo_user_id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
  
GRANT ALL ON FreeWeibo.Weibo_User_data TO 'admin'@'localhost';
