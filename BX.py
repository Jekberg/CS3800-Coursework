import os
import subprocess
import sys

home_dir = os.environ["HOME"]
data_dir = f"{home_dir}/CS3800-Coursework/Datasets"
script_dir = f"{home_dir}/CS3800-Coursework/hive"
hdfs_output_dir = '/user/BX/output'

def main():
	routine = {}
	routine["setup"] = setup
	routine["most-rated-books"] = most_rated_books
	routine["top-100-books"] = top_100_books
	routine["abc"] = abc
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

def rating_summary():
	subprocess.run(['hdfs', 'dfs', '-mkdir', '-p', hdfs_output_dir])
	hive_script_arg = f"HIVE_SCRIPT_DIR={script_dir}"
	hdfs_output_dir_arg = f"HDFS_OUTPUT_DIR={hdfs_output_dir}"
	run_hive_file(f"{script_dir}/BookRatingSummary.hql", hive_script_arg, hdfs_output_dir_arg)

def abc():
	run_hive_file(f"{script_dir}/UserBookRecomendations.hql")

def top_100_books():
	subprocess.run(['hdfs', 'dfs', '-mkdir', '-p', hdfs_output_dir])
	hive_script_arg = f"HIVE_SCRIPT_DIR={script_dir}"
	hdfs_output_dir_arg = f"HDFS_OUTPUT_DIR={hdfs_output_dir}"
	run_hive_file(f"{script_dir}/Top100Books.hql", hive_script_arg, hdfs_output_dir_arg)

if __name__ == '__main__':
	main()
