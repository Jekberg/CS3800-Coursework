import html
import os
import subprocess

def tidy(inpath, outpath, delim):
	with open(inpath, 'r', errors = 'ignore') as infile:
		# Skip the headers
		infile.readline()
		with open(outpath, 'w') as outfile:
			for line in infile:
				# Remove special encodings (HTML escapes) from the datasets
				# and replace quoted fields
				line = html.unescape(line)
				line = line.replace('"', '')
				outfile.write(line)

current_path = os.getcwd()
temp_dir = f'{current_path}/.temp'
dataset_dir = f"{current_path}/Datasets"
subprocess.run(['mkdir', '-p', f'{temp_dir}'])

tidy(f"{dataset_dir}/BX-Users.csv", f"{temp_dir}/BX-Users.csv.tidy", ';')
tidy(f"{dataset_dir}/BX-Book-Ratings.csv", f"{temp_dir}/BX-Book-Ratings.csv.tidy", ';')
tidy(f"{dataset_dir}/BX-Books.csv", f"{temp_dir}/BX-Books.csv.tidy", ';')

query = """
DROP DATABASE IF EXISTS CS3800 CASCADE;
CREATE DATABASE CS3800;
USE CS3800;

-- Setup the tables representing the datasets
DROP TABLE IF EXISTS Users;
CREATE TABLE Users(
	id int,
	location string,
	age int)
COMMENT 'The BX users'
CLUSTERED BY (id)
SORTED BY (id ASC)
INTO 256 BUCKETS
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\\073'
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
COMMENT 'The BX books'
CLUSTERED BY (isbn)
SORTED BY (isbn ASC)
INTO 256 BUCKETS
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\\073'
STORED AS textfile;

DROP TABLE IF EXISTS Ratings;
CREATE TABLE IF NOT EXISTS Ratings (
	userId int,
	isbn string,
	rating int)
COMMENT 'The BX book-ratings'
CLUSTERED BY (userId, isbn)
SORTED BY (userId ASC, isbn ASC)
INTO 256 BUCKETS
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\\073'
STORED AS textfile;

-- Create table index
CREATE INDEX Users_Id_Index
ON TABLE Users(id) AS 'COMPACT'
WITH DEFERRED REBUILD;

CREATE INDEX Books_Isbn_Index
ON TABLE Books(isbn) AS 'COMPACT'
WITH DEFERRED REBUILD;

-- Import the BX datasets.
LOAD DATA LOCAL INPATH '${DATASET_PATH}/BX-Users.csv.tidy' OVERWRITE INTO TABLE Users;
LOAD DATA LOCAL INPATH '${DATASET_PATH}/BX-Books.csv.tidy' OVERWRITE INTO TABLE Books;
LOAD DATA LOCAL INPATH '${DATASET_PATH}/BX-Book-Ratings.csv.tidy' OVERWRITE INTO TABLE Ratings;
"""

hive_home = os.environ["HIVE_HOME"]
subprocess.run(['hive', '-e', query, "--hivevar", f"DATASET_PATH={temp_dir}"], cwd = hive_home)

