# CS3800-Coursework
Scripts related to the CS3800 coursework


## Prerequesits
- Hadoop 2.7.3
- Hive 2.1.1
- Python 3.6

## Start The Application
The application is started by starting HDFS and YARN using the command ```bash Start.sh``` in the CS3800-Coursework directory. Then the BX dataset can be loaded into the application by executing ```python3 Setup-BX.py```, which will create the database if it does not exist.

## Stop The Application
Stop the application by issuing the command ```bash Stop.sh``` in the CS3800-Coursework directory. To delete the database, run the command ```python3 Teardown-BX.py``` **BEFORE** stopping the HDFS and YARN.

## Using the Application
