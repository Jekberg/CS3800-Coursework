USE CS3800;

DROP TABLE IF EXISTS BookRatingSummary;
CREATE TABLE IF NOT EXISTS BookRatingSummary (
	isbn string,
	ratingCount int,
	minRating int,
	maxRating int,
	avgRating float,
	stDev float);

TRUNCATE TABLE BookRatingSummary;

INSERT INTO BookRatingSummary
SELECT
	Summary.isbn,
	Summary.ratingCount,
	Summary.ratingMin,
	Summary.ratingMax,
	Summary.ratingAvg,
	SQRT(SUM(POW(R.rating - Summary.ratingAvg, 2)) / (Summary.ratingCount - 1))
FROM (
	SELECT
		isbn,
		COUNT(userId) AS ratingCount,
		MIN(rating) AS ratingMin,
		MAX(rating) AS ratingMax,
		AVG(rating) AS ratingAvg
	FROM Ratings
	GROUP BY isbn) AS Summary
INNER JOIN Ratings AS R ON R.isbn = Summary.isbn
GROUP BY
	Summary.isbn,
	Summary.ratingCount,
	Summary.ratingMin,
	Summary.ratingMax,
	Summary.ratingAvg;