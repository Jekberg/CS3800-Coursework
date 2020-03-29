USE CS3800;

SET hive.auto.convert.join = false;

-- Based on Naieve Bayes
WITH BookRatingCount AS (
	SELECT isbn, COUNT(userId) AS count
	FROM Ratings
	GROUP BY isbn)
, BookRatingCountGivenAge AS (
	SELECT R.isbn, COUNT(R.isbn) AS count
	FROM Ratings AS R
	INNER JOIN Users AS U ON U.id = R.userId
	WHERE U.age = ${AGE}
	GROUP BY R.isbn)
SELECT
	Rankings.bookProbabillityByAge * Rankings.bookProbabillity AS rank,
	B.title,
	B.author,
	B.publisher,
	B.isbn
FROM (
	SELECT
		BRC.isbn,
		BRCGA.count / SUM(BRCGA.count) OVER () AS bookProbabillityByAge,
		BRC.count / SUM(BRC.count) OVER () AS bookProbabillity
	FROM BookRatingCount AS BRC
	INNER JOIN BookRatingCountGivenAge AS BRCGA ON BRCGA.isbn = BRC.isbn)
	AS Rankings
INNER JOIN Books AS B ON B.isbn = Rankings.isbn
SORT BY rank DESC
LIMIT 10;
