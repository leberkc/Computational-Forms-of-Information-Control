USE FreeWeibo;

CREATE TABLE Weibo_HotTerm_Topic_Post (
hotterm VARCHAR(100),
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

GRANT ALL ON FreeWeibo.Weibo_HotTerm_Topic_Post TO 'admin'@'localhost';
