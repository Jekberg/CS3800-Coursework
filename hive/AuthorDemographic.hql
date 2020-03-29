USE CS3800;

SET hive.auto.convert.join = false;

--WITH AuthorAgeSummary AS (
--	SELECT
--		B.author,
--		U.age,
--		COUNT(U.id) AS ageCount
--	FROM Users AS U
--	INNER JOIN Ratings AS R ON R.userId = U.id
--	INNER JOIN Books AS B on B.isbn = R.isbn
--	GROUP BY
--		B.author,
--		U.age)
--SELECT
--	author,
--	age,
--	ageCount / SUM(ageCount) OVER(PARTITION BY author)
--FROM AuthorAgeSummary
--SORT BY
--	author,
--	age;




