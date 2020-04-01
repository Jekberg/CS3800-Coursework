USE CS3800;

SET hive.auto.convert.join = false;
SET hive.cli.print.header = true;

WITH BookAssociations AS (
	SELECT
		B.title,
		B.author,
		B.publisher,
		B.isbn,
		COUNT(B.isbn) as associationCount
	FROM Ratings AS R1
	INNER JOIN Ratings AS R2 ON R2.userId = R1.userId
	INNER JOIN Books AS B ON B.isbn = R2.isbn
	WHERE R1.isbn = '${ISBN}'
		AND R1.isbn <> R2.isbn
	GROUP BY
		B.title,
		B.author,
		B.publisher,
		B.isbn
	SORT BY associationCount DESC)
SELECT
	title,
	author,
	publisher,
	isbn
FROM BookAssociations
LIMIT 10;
