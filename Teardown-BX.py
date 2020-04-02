import os
import subprocess

query = "DROP DATABASE IF EXISTS CS3800 CASCADE;"
hive_home = os.environ["HIVE_HOME"]
subprocess.run(['hive', '-e', query, "--hivevar", f"DATASET_PATH={hive_home}"], cwd = hive_home)
