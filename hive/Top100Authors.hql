--in order to get the popular authors, we need to find books that have high average ratings * the number of responses
USE CS3800;

SET hive.auto.convert.join = false;
SET hive.cli.print.header = true;
WITH BookRankings AS (
	SELECT
		UCASE(B.author) AS author,	
		AVG(R.rating) * COUNT(R.userId) AS relevence, 
		AVG(R.rating) AS avgRating,
		B.title,
		B.publisher,
		B.isbn
	FROM Books AS B
	INNER JOIN Ratings AS R ON R.isbn = B.isbn
	GROUP BY
		author,
		B.title,
		B.publisher,
		B.isbn
	SORT BY
		avgRating DESC,
		relevence DESC,
		author DESC
)
SELECT
	author,
	average_Rating
FROM (
SELECT
	author,
 	AVG(avgRating) AS average_Rating,
	relevence
FROM BookRankings
GROUP BY
	author,
	relevence,
	avgRating
SORT BY
	average_Rating DESC,
	relevence DESC
LIMIT 100
) popularAuthors
;