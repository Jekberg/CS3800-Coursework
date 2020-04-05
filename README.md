# CS3800-Coursework
## Prerequesits
- Java 8
- Hadoop 2.7.3
- Hive 2.1.1
- Python 3.6

## Before Using the Applcation
Before the application is used, the first action to be taken is to navigate into the directory of the project  by running ```cd CS3800-Coursework``` in the parent directory. This is because the root directory of the application is used for finding the appropriate subfolders. Also ensure that *HIVE_HOME* is an  environmental variable set to point tot the root hive directory.

## Start The Application
The application is started by starting HDFS and YARN using the command ```bash Start.sh``` in the CS3800-Coursework directory. Then the BX dataset can be loaded into the application by executing ```python3 Setup-BX.py```, which will create the database if it does not exist.

## Stop The Application
Stop the application by issuing the command ```bash Stop.sh``` in the CS3800-Coursework directory. To delete the database, run the command ```python3 Teardown-BX.py``` **BEFORE** stopping the HDFS and YARN.

## Using the Application
The *BX.py* file is the script which functions as the command line interface of the application. The script contains a number of services which can be invoked to generate reports using the BX dataset. An example of how to get the top 100 books with the overall best ratings can be obtained by typing ```python3 BX.py top-100-books```, which run a hive query ad output the results in the terminal.

For a list of the available commands, type ```python3 BX.py help```; however, be aware that some sscripts require additional arguments to be provides, such as the *books-also-rated-with* command, which require an ISBN as an extra argument. The commands which depend on additional arguments will alert the user that an extra argument is needed if invoked without the oppropriate number of arguments.
