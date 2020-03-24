DROP DATABASE IF EXISTS CS3800 CASCADE;
CREATE DATABASE CS3800;
USE CS3800;

-- Setup the tables representing the datasets
DROP TABLE IF EXISTS Users;
CREATE TABLE Users(
	id int,
	location string,
	age int)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\073'
STORED AS textfile;

DROP TABLE IF EXISTS Books;
CREATE TABLE IF NOT EXISTS Books (
	isbn string,
	title string,
	author string,
	yearOfPublication string,
	publisher string,
	smallImageUrl string,
	mediumImageUrl string,
	largeImageUrl string)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\073'
STORED AS textfile;

DROP TABLE IF EXISTS Ratings;
CREATE TABLE IF NOT EXISTS Ratings(
	userId int,
	isbn string,
	rating int)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\073'
STORED AS textfile;

-- Import the BX datasets.
LOAD DATA LOCAL INPATH '${DATASET_PATH}/BX-Users.csv.tidy' OVERWRITE INTO TABLE Users;
LOAD DATA LOCAL INPATH '${DATASET_PATH}/BX-Books.csv.tidy' OVERWRITE INTO TABLE Books;
LOAD DATA LOCAL INPATH '${DATASET_PATH}/BX-Book-Ratings.csv.tidy' OVERWRITE INTO TABLE Ratings;
