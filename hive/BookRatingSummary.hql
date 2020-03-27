USE CS3800;

SELECT
	U.id,
	B.author,
	AVG(R.rating)
FROM Users AS U
INNER JOIN Ratings AS R ON R.userId = U.id
INNER JOIN Books AS B ON B.isbn = R.isbn
GROUP BY
	U.id,
	B.author
