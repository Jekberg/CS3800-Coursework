USE CS3800;

SET hive.auto.convert.join = false;

--SELECT U.id, B.isbn
--FROM Users AS U
--FULL OUTER JOIN Books AS B;

WITH RatingCountByAgeGroup AS (
	SELECT U.age, COUNT(R.isbn) AS ratingCount
	FROM Users AS U
	INNER JOIN Ratings AS R ON R.userId = U.id
	GROUP BY U.age)
SELECT
	ratingCount / SUM(ratingCount) OVER () AS ratio,
	age
FROM RatingCountByAgeGroup
SORT BY
	ratio DESC,
	age ASC;
