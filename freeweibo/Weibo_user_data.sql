USE FreeWeibo;

CREATE TABLE Weibo_User_data (
weibo_user_id VARCHAR(20),
screen_name VARCHAR(100),
profile_url TINYTEXT,
#verified_reason TINYTEXT,
#u_description VARCHAR(255),
gender char,
followers_count INT,
follow_count INT,
time_scrapped DATETIME,
PRIMARY KEY(weibo_user_id, screen_name)
)ENGINE = InnoDB

ALTER TABLE `FreeWeibo`.`Weibo_User_data` 
ADD CONSTRAINT `fk_user`
  FOREIGN KEY (`weibo_user_id`)
  REFERENCES `FreeWeibo`.`FreeWeiboPosts` (`weibo_id_user`)
  ON DELETE CASCADE
  ON UPDATE NO ACTION;

GRANT ALL ON FreeWeibo.Weibo_User_data TO 'admin'@'localhost';
