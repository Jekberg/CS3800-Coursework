USE CS3800;

SELECT
	B.isbn,
	B.title,
	B.author,
	COUNT(R.userId) AS Ratings
FROM Books AS B
INNER JOIN Ratings AS R ON R.isbn = B.isbn
GROUP BY
	B.isbn,
	B.title,
	B.author
SORT BY Ratings DESC
LIMIT 10;
