import subprocess

hdfs_base_dir = '/user/BX/'
hdfs_input_dir = f'{hdfs_base_dir}/input'
hdfs_output_dir = f'{hdfs_base_dir}/output'


subprocess.run(['hdfs', 'dfs', '-mkdir', '-p', hdfs_input_dir])
subprocess.run(['hdfs', 'dfs', '-mkdir', '-p', hdfs_output_dir])
#subprocess.run(['hdfs', 'dfs', '-put'])

