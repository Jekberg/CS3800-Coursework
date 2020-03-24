import os
import subprocess
import sys

home_dir = os.environ["HOME"]
data_dir = f"{home_dir}/CS3800-Coursework/Datasets"
script_dir = f"{home_dir}/CS3800-Coursework/hive"

def main():
	routine = {}
	routine["setup"] = setup
	routine["most-rated-books"] = most_rated_books
	routine["x"] = x
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

def setup():
	datasetpath = f"DATASET_PATH={data_dir}"
	run_hive_file(f"{script_dir}/Setup.hql", datasetpath)

def most_rated_books():
	run_hive_file(f"{script_dir}/MostReviewedBooks.hql")

def x():
	hive_script_arg = f"HIVE_SCRIPT_DIR={script_dir}"
	run_hive_file(f"{script_dir}/X.hql", hive_script_arg)

if __name__ == '__main__':
	main()
