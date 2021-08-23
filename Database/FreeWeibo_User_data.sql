USE FreeWeibo;

CREATE TABLE FreeWeibo_User_data (
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
PRIMARY KEY(weibo_user_id)
)ENGINE = InnoDB

ALTER TABLE `FreeWeibo`.`FreeWeibo_User_data` 
ADD CONSTRAINT `fk_FreeWeibo_User`
  FOREIGN KEY (`weibo_user_id`)
  REFERENCES `FreeWeibo`.`FreeWeiboPosts` (`weibo_user_id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

#Add Column Containing Status of the weibo users 
ALTER TABLE FreeWeibo_User_data
ADD COLUMN active_status BOOLEAN AFTER origin;

GRANT ALL ON FreeWeibo.FreeWeibo_User_data TO 'admin'@'localhost';
