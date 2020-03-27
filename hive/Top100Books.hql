USE CS3800;

SET hive.auto.convert.join = false;

CREATE EXTERNAL TABLE IF NOT EXISTS Top100Books (
	rated float,
	reviews int,
	title string,
	author string,
	publisher string,
	isbn string)
COMMENT ''
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\073'
STORED AS TEXTFILE
LOCATION '${HDFS_OUTPUT_DIR}/Top100Books';

WITH BookRankings AS (
	SELECT
		AVG(R.rating) * COUNT(R.userId) AS relevence, 
		AVG(R.rating) AS avgRating,
		COUNT(R.userId) ratingCount,
		B.title,
		B.author,	
		B.publisher,
		B.isbn
	FROM Books AS B
	INNER JOIN Ratings AS R ON R.isbn = B.isbn
	GROUP BY
		B.title,
		B.author,	
		B.publisher,
		B.isbn
	SORT BY
		relevence DESC,
		avgRating DESC
	LIMIT 100)
INSERT OVERWRITE TABLE Top100Books
SELECT
	avgRating,
	ratingCount,
	title,
	author,	
	publisher,
	isbn
FROM BookRankings;

