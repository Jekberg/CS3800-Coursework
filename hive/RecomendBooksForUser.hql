USE CS3800;

SET hive.auto.convert.join = false;
SET hive.cli.print.header = true;

WITH RatedAuthors AS (
	SELECT R.userId, R.isbn, B.author, R.rating
	FROM Ratings AS R
	INNER JOIN Books AS B ON B.isbn = R.isbn
	WHERE r.UserId = ${USER_ID})
SELECT title, author, publisher, isbn
FROM (
	SELECT
		B.title,
		B.author,
		B.publisher,
		B.isbn,
		SUM(RA.rating) OVER(PARTITION BY UCASE(RA.author)) AS totalRatings
	FROM Books AS B
	INNER JOIN RatedAuthors AS RA ON UCASE(RA.author) = UCASE(B.author)
	WHERE RA.isbn <> B.isbn
	SORT BY totalRatings DESC) AS Results
LIMIT 50;
