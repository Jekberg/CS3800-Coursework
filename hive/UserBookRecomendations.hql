USE CS3800;

SET hive.auto.convert.join = false;

SELECT U.id, B.isbn
FROM Users AS U
FULL OUTER JOIN Books AS B;
