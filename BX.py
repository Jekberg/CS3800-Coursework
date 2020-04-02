import os
import subprocess
import sys

home_dir = os.environ["HOME"]
script_dir = f"{home_dir}/CS3800-Coursework/hive"

def main():
	routine = {}
	routine["top-100-authors"] = top_100_authors
	routine["top-100-books"] = top_100_books
	routine["recomend-books-for-user"] = recomend_books_for_user
	routine["book-recomendations-for-age"] = book_recomendations_for_age
	routine["books-also-rated-with"] = book_also_rated_with
	if sys.argv[1] in routine:	
		routine[sys.argv[1]]()
	else:
		print("Invalid command: ", sys.argv[1])
		print("These are the valid commands")
		for command in routine.keys():
			print(command)

def run_hive_file(file, *args):
	hive_dir = os.environ["HIVE_HOME"]
	hive_args = [['--hivevar', str(arg)] for arg in args]
	hive_args = [arg for arglist in hive_args for arg in arglist]
	result = subprocess.run(["hive", "-f", file] + hive_args, cwd = hive_dir)
	result.check_returncode()
	return result.stdout

def top_100_books():
	run_hive_file(f"{script_dir}/Top100Books.hql")

def top_100_authors():
	run_hive_file(f"{script_dir}/Top100Authors.hql")

def recomend_books_for_user():
	if len(sys.argv) < 3:
		print('User ID needed!')
		print('Please provide a user ID number.')
		return
	id = int(sys.argv[2])
	run_hive_file(f"{script_dir}/RecomendBooksForUser.hql", f"USER_ID={id}")

def book_recomendations_for_age():
	if len(sys.argv) < 3:
		print('Age needed!')
		print('Please provide a age number.')
		return
	age = int(sys.argv[2])
	run_hive_file(f"{script_dir}/BookRecomendationsByAge.hql", f"AGE={age}")

def book_also_rated_with():
	if len(sys.argv) < 3:
		print('Book ISBN needed!')
		print('Please provide a book ISBN.')
		return
	isbn = sys.argv[2]
	run_hive_file(f"{script_dir}/BookAlsoRatedWithBook.hql", f"ISBN={isbn}")

if __name__ == '__main__':
	main()
