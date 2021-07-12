CREATE DATABASE FreeWeibo;

USE FreeWeibo;

CREATE TABLE FreeWeiboPosts (
Post_Id INT NOT NULL AUTO_INCREMENT,
User_name VARCHAR(50),
FreeWeibo_Post_Id TINYTEXT NOT NULL,
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


