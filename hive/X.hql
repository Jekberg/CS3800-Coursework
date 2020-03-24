USE CS3800;

IF TABLE NOT EXISTS BookRatingSummary
THEN
	source ${HIVE_SCRIPT_DIR}/BookRatingSummary.hql;
END;

--source ${HIVE_SCRIPT_DIR}/BookRatingSummary.hql;
--SELECT *
--FROM BookRatingSummary
--WHERE 1 < ratingCount
--SORT BY
--	ratingCount DESC,
--	avgRating DESC,
--	stDev ASC
--LIMIT 10;


