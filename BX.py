import os
import subprocess
import sys

home_dir = os.environ["HOME"]
data_dir = f"DATASET_PATH={home_dir}/CS3800-Coursework/Datasets"
script_dir = f"{home_dir}/CS3800-Coursework/hive"

def main():
	routine = {}
	routine["setup"] = setup
	routine["book-recomendations-by-author"] = book_recomendations_by_author
	routine[sys.argv[1]]()

def run_hive_file(file, *args):
	hive_dir = os.environ["HIVE_HOME"]
	hive_args = [['--hivevar', str(arg)] for arg in args]
	hive_args = [arg for arglist in hive_args for arg in arglist]
	subprocess.call(["hive", "-f", file] + hive_args, cwd = hive_dir)

def setup():
	datasetpath = f"DATASET_PATH={data_dir}"
	run_hive_file(f"{script_dir}/Setup.hql", datasetpath)

def book_recomendations_by_author():
	run_hive_file(f"{script_dir}/BookRecomendationsByAuthor.hql")

#def x():
#	run_hive_command("""
#	USE CS3800;
#	WITH UserAuthorRatings AS (
#		SELECT
#			R.userId,
#			B.isbn,
#			B.author,
#			R.rating
#		FROM Ratings AS R
#		INNER JOIN Books AS B ON B.isbn = R.isbn)
#	SELECT
#		Result.userId,
#		Result.isbn,
#		Result.title,
#		Result.author
#	FROM (
#		SELECT
#			UAR.userId,
#			B.isbn,
#			B.title,
#			B.author,
#			AVG(UAR.rating) AS rating
#		FROM Books AS B
#		INNER JOIN UserAuthorRatings AS UAR ON UAR.author = B.author
#		WHERE UAR.isbn <> B.isbn
#		GROUP BY
#			UAR.userId,
#			B.isbn,
#			B.title,
#			B.author
#		SORT BY rating DESC)
#	AS Result
#	UNION DISTINCT
#	SELECT ;
#	""")

#def top_book_ratings():
#	run_hive_command("""
#	USE CS3800;
#
#	CREATE TABLE IF NOT EXISTS BookRatingSummary(
#		isbn string,
#		ratingCount int,
#		ratingAvg float,
#		ratingMin int,
#		ratingMax int)
#	ROW FORMAT DELIMITED
#	FIELDS TERMINATED BY '\073'
#	STORED AS TEXTFILE;
#
#	INSERT INTO BookRatingSummary
#	SELECT
#		B.isbn,
#		COUNT(R.user_id) AS RatingCount,
#		AVG(R.rating) AS AvgRating,
#		MIN(R.rating) AS MinRating,
#		MAX(R.rating) AS MaxRating
#	FROM Books AS B
#	INNER JOIN Ratings AS R ON R.isbn = B.isbn
#	GROUP BY B.isbn
#	SORT BY AvgRating DESC;
#	""")

if __name__ == '__main__':
	main()
