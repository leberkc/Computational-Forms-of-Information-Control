USE FreeWeiboPosts;

CREATE TABLE Posts (
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
content TEXT,
hashtags TINYTEXT,
hashtagsurls TEXT,
time_scrapped DATETIME,
PRIMARY KEY(Post_Id)
);