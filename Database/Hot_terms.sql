CREATE DATABASE FreeWeibo;

USE FreeWeibo;

CREATE TABLE HOTTERMS (
Hot_Term_Id INT NOT NULL AUTO_INCREMENT,
HotTerm VARCHAR(255),
first_time_scrapped DATETIME,
last_time_scrapped DATETIME,
PRIMARY KEY(Hot_Term_Id)
)ENGINE = InnoDB;

GRANT ALL ON FreeWeibo.HOTTERMS TO 'admin'@'localhost';

ALTER TABLE `FreeWeibo`.`HOTTERMS` 
ADD UNIQUE INDEX `HotTerm_UNIQUE` (`HotTerm` ASC) VISIBLE;
;
