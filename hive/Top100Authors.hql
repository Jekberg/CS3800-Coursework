USE CS3800;

SET hive.auto.convert.join = false;
SET hive.cli.print.header = true;

WITH BookRankings AS (
	SELECT
		UCASE(B.author) AS author,	
		AVG(R.rating) * COUNT(R.userId) AS relevence, 
		AVG(R.rating) AS avgRating
	FROM Books AS B
	INNER JOIN Ratings AS R ON R.isbn = B.isbn
	GROUP BY author
	SORT BY
 		relevence DESC,
		avgRating DESC
	LIMIT 100)
SELECT
	author,
	avgRating
FROM BookRankings
SORT BY avgRating DESC;
