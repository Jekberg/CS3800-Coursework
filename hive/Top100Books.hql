USE CS3800;

SET hive.auto.convert.join = false;
SET hive.cli.print.header = true;

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
SELECT
	title,
	author,	
	publisher,
	isbn
FROM BookRankings;

