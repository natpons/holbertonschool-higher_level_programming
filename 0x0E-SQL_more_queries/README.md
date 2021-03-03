# 0x0E. SQL - More queries

-   Foundations - Higher-level programming  Databases
-   By Guillaume, CTO at Holberton School

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/66988091.jpg)

## Resources

**Read or watch**:

-   [How To Create a New User and Grant Permissions in MySQL](https://intranet.hbtn.io/rltoken/u4h2MXcCQfadszlRMQy-gw "How To Create a New User and Grant Permissions in MySQL")
-   [How To Use MySQL GRANT Statement To Grant Privileges To a User](https://intranet.hbtn.io/rltoken/ztrEKQexfEDtZ-8EUsG70Q "How To Use MySQL GRANT Statement To Grant Privileges To a User")
-   [MySQL constraints](https://intranet.hbtn.io/rltoken/LBrFqCMm9N9woTX7sS7e0g "MySQL constraints")
-   [SQL technique: subqueries](https://intranet.hbtn.io/rltoken/YYpPtkqFeKSCsAU4Y_y3Og "SQL technique: subqueries")
-   [Basic query operation: the join](https://intranet.hbtn.io/rltoken/npLCp3WasK0SUSUQqCF25A "Basic query operation: the join")
-   [SQL technique: multiple joins and the distinct keyword](https://intranet.hbtn.io/rltoken/GmRLMhkY-pPvjcpzyDvmRg "SQL technique: multiple joins and the distinct keyword")
-   [SQL technique: join types](https://intranet.hbtn.io/rltoken/ryjyRRN7696rJV0maP03Xw "SQL technique: join types")
-   [SQL technique: union and minus](https://intranet.hbtn.io/rltoken/L7Fi5w8GZG5MSdQZ19e88g "SQL technique: union and minus")
-   [MySQL Cheat Sheet](https://intranet.hbtn.io/rltoken/V9vpLbtkFwV4EZYoiz2NBA "MySQL Cheat Sheet")
-   [The Seven Types of SQL Joins](https://intranet.hbtn.io/rltoken/ySKSdhFeMDddea07XrDzeQ "The Seven Types of SQL Joins")
-   [MySQL Tutorial](https://intranet.hbtn.io/rltoken/-uqP0a89xUl3SsmV_ZtxRA "MySQL Tutorial")
-   [SQL Style Guide](https://intranet.hbtn.io/rltoken/jn4SHgwVtOJF0LQYPEIs-g "SQL Style Guide")
-   [MySQL 5.7 SQL Statement Syntax](https://intranet.hbtn.io/rltoken/YjNAE7DcadDbT_a7iI0sYw "MySQL 5.7 SQL Statement Syntax")

Extra resources around relational database model design:

-   [Design](https://intranet.hbtn.io/rltoken/9ppVdXqFMn-v1eKuxsOvaQ "Design")
-   [Normalization](https://intranet.hbtn.io/rltoken/zo6dqYxsXby3S3uON5JfOg "Normalization")
-   [ER Modeling](https://intranet.hbtn.io/rltoken/ZaMMezT-GdpgHB9pmM78iw "ER Modeling")

## Learning Objectives

At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/wFSyv4XqA1VTJynauL7NLg "explain to anyone"),  **without the help of Google**:

### General

-   How to create a new MySQL user
-   How to manage privileges for a user to a database or table
-   Whats a  `PRIMARY KEY`
-   Whats a  `FOREIGN KEY`
-   How to use  `NOT NULL`  and  `UNIQUE`  constraints
-   How to retrieve datas from multiple tables in one request
-   What are subqueries
-   What are  `JOIN`  and  `UNION`

## Requirements

### General

-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files will be executed on Ubuntu 14.04 LTS using  `MySQL 5.7`  (version 5.7.8-rc)
-   All your files should end with a new line
-   All your SQL queries should have a comment just before (i.e. syntax above)
-   All your files should start by a comment describing the task
-   All SQL keywords should be in uppercase (`SELECT`,  `WHERE`)
-   A  `README.md`  file, at the root of the folder of the project, is mandatory
-   The length of your files will be tested using  `wc`

## More Info

### Comments for your SQL file:

```
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$

```

### Install MySQL 5.7 on Ubuntu 14.04 LTS

```
$ echo 'deb http://repo.mysql.com/apt/ubuntu/ trusty mysql-5.7-dmr' | sudo tee -a /etc/apt/sources.list
$ sudo apt-get update
$ sudo apt-get install mysql-server-5.7
...
$ mysql --version
mysql  Ver 14.14 Distrib 5.7.8-rc, for Linux (x86_64) using  EditLine wrapper
$

```

**Dont forget your  `root`  password**

If you had before MySQL 5.5 installed, please run these 2 commands after the installation of the version 5.7:

```
$ mysql_upgrade -u root -p
Password: 
$ sudo service mysql restart

```

If you have some issues to upgrade to 5.7, dont hesitate to cleanup your server of any MySQL packages:  `sudo apt-get remove --purge mysql-server mysql-client mysql-common`

### Use container-on-demand to run MySQL

-   Ask for container  `Ubuntu 14.04 - Python 3.4`
-   Connect via SSH
-   Or via the WebTerminal
-   In the container, you should start MySQL before playing with it:

```
$ service mysql start
* MySQL Community Server 5.7.8-rc is started
$
 $ cat 0-list_databases.sql | mysql -uroot -p my_database
 Enter password: 
 Database
 information_schema
 mysql
 performance_schema
 sys
 $

 ```

 **In the container, credentials are  `root/root`**

### How to import a SQL dump

 ```
 $ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
 Enter password: 
 $ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
 Enter password: 
 $ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
 Enter password: 
 id  name
 1   Drama
 2   Mystery
 3   Adventure
 4   Fantasy
 5   Comedy
 6   Crime
 7   Suspense
 8   Thriller


 ```

 ![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/3/bc2575fee3303b731031.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210302%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210302T073418Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=af7cde780e7607208f9b5c5c35a10b9e88b9e60477bb6b3be00c63aef012a610)

### Memo

#### [](https://github.com/Battsetseg20/holbertonschool-higher_level_programming/tree/main/0x0E-SQL_more_queries#useful-commands-for-task-8)Useful commands for Task 8

 To Insert values into table

 ```
 echo 'INSERT INTO cities (id, state_id, name) VALUES (2, 1, "San Jose");' | mysql -hlocalhost -uroot -p hbtn_0d_usa


 ```

#### [](https://github.com/Battsetseg20/holbertonschool-higher_level_programming/tree/main/0x0E-SQL_more_queries#useful-commands-for-from-task-10-to-18)Useful commands for from Task 10 to 18

 -   To start mysql

 ```
 $ mysql -hlocalhost -uroot -p
 Password: 


 ```

 -   To import a SQL dump

 ```
 $ mysql> use database_name;
 $ mysql> source file.sql;

 ```

 OR

 ```
 $ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
 Enter password: 
 $ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
 Enter password: 


 ```

 -   To see databases in server

 ```
 mysql> SHOW DATABASES;
 +--------------------+
 | Database           |
 +--------------------+
 | information_schema |
 | hbtn_0c_0          |
 | hbtn_0d_2          |
 | hbtn_0d_tvshows    |
 | hbtn_0d_usa        |
 | mysql              |
 | performance_schema |
 | sys                |
 +--------------------+
 8 rows in set (0.00 sec)

	```

	OR

	```
	SHOW DATABASES | mysql -hlocalhost -uroot -p
	Enter password: 

	```

	-   To see the list of tables in particular database

	```
	mysql> SHOW TABLES FROM hbtn_0d_tvshows;
	+---------------------------+
	| Tables_in_hbtn_0d_tvshows |
	+---------------------------+
	| tv_genres                 |
	| tv_show_genres            |
	| tv_shows                  |
	+---------------------------+
	3 rows in set (0.00 sec)

	```

	OR

	```
	$ SHOW TABLES | mysql -hlocalhost -uroot -p hbtn_0d_tvshows

	```

	-   To see the content of a particular table (table  `tv_genres`from  `hbtn_0d_tvshows`)

	```
	mysql> USE hbtn_0d_tvshows ;
	       Reading table information for completion of table and column names
	              You can turn off this feature to get a quicker startup with -A

		             Database changed

			     mysql> SELECT * FROM tv_genres;
			     +----+-----------+
			     | id | name      |
			     +----+-----------+
			     |  1 | Drama     |
			     |  2 | Mystery   |
			     |  3 | Adventure |
			     |  4 | Fantasy   |
			     |  5 | Comedy    |
			     |  6 | Crime     |
			     |  7 | Suspense  |
			     |  8 | Thriller  |
			     +----+-----------+
			     8 rows in set (0.00 sec)

	```

	ÒR

	```
	$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows

	```

	```
	$ echo 'SELECT * FROM tv_shows;' | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
	$ Enter password: 
	id    title
	1     House
	2     Game of Thrones
	3     The Big Bang Theory
	4     New Girl
	5     Silicon Valley
	6     Breaking Bad
	7     Better Call Saul
	8     Dexter
	9     Homeland
	10    The Last Man on Earth

	```

	```
	$ echo 'SELECT * FROM tv_show_genres;' | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
	$ Enter password: 
	show_id		genre_id
	1			1
	1			2
	2			3
	2			1
	2			4
	3			5
	4			5
	5			5
	6			6
	6			1
	6			7
	6			8
	8			6
	8			1
	8			2
	8			7
	8			8
	10			5
	10			1

	```

#### [](https://github.com/Battsetseg20/holbertonschool-higher_level_programming/tree/main/0x0E-SQL_more_queries#useful-commands-for-from-task-19-to-20)Useful commands for from Task 19 to 20

	```
	mysql> SHOW DATABASES;
	+----------------------+
	| Database             |
	+----------------------+
	| information_schema   |
	| hbtn_0c_0            |
	| hbtn_0d_2            |
	| hbtn_0d_tvshows      |
	| hbtn_0d_tvshows_rate |
	| hbtn_0d_usa          |
	| mysql                |
	| performance_schema   |
	| sys                  |
	+----------------------+
	9 rows in set (0.00 sec)

	```

	```
	mysql> SHOW TABLES FROM hbtn_0d_tvshows_rate;
	+--------------------------------+
	| Tables_in_hbtn_0d_tvshows_rate |
	+--------------------------------+
	| tv_genres                      |
	| tv_show_genres                 |
	| tv_show_ratings                |
	| tv_shows                       |
	+--------------------------------+
	4 rows in set (0.00 sec)

	```

	```
	mysql> USE hbtn_0d_tvshows_rate;
	Reading table information for completion of table and column names
	You can turn off this feature to get a quicker startup with -A

	Database changed
	mysql> SELECT * FROM tv_genres;
	+----+-----------+
	| id | name      |
	+----+-----------+
	|  1 | Drama     |
	|  2 | Mystery   |
	|  3 | Adventure |
	|  4 | Fantasy   |
	|  5 | Comedy    |
	|  6 | Crime     |
	|  7 | Suspense  |
	|  8 | Thriller  |
	+----+-----------+
	8 rows in set (0.00 sec)

	```

	```
	mysql> SELECT * FROM tv_show_genres;
	+---------+----------+
	| show_id | genre_id |
	+---------+----------+
	|       2 |        1 |
	|       2 |        2 |
	|       3 |        3 |
	|       3 |        1 |
	|       3 |        4 |
	|       4 |        5 |
	|       5 |        5 |
	|       6 |        5 |
	|       7 |        6 |
	|       7 |        1 |
	|       7 |        7 |
	|       7 |        8 |
	|       9 |        6 |
	|       9 |        1 |
	|       9 |        2 |
	|       9 |        7 |
	|       9 |        8 |
	|      11 |        5 |
	|      11 |        1 |
	+---------+----------+
	19 rows in set (0.00 sec)

	```

	```

	mysql> SELECT * FROM tv_show_ratings;

	+---------+------+
	| show_id | rate |
	+---------+------+
	|       2 |    0 |
	|       2 |    1 |
	|       2 |    2 |
	|       2 |    3 |
	|       2 |    4 |
	|       2 |    5 |
	|       2 |    6 |
	|       3 |    0 |
	|       3 |    1 |
	|       3 |    2 |
	|       3 |    0 |
	|       3 |    0 |
	|       3 |    1 |
	|       3 |    2 |
	|       3 |    0 |
	|       3 |    0 |
	|       3 |    1 |
	|       3 |    2 |
	|       3 |    3 |
	|       3 |    4 |
	|       3 |    0 |
	|       3 |    1 |
	|       3 |    2 |
	|       3 |    3 |
	|       3 |    4 |
	|       3 |    5 |
	|       3 |    6 |
	|       3 |    7 |
	|       3 |    8 |
	|       3 |    0 |
	|       3 |    1 |
	|       3 |    2 |
	|       3 |    0 |
	|       3 |    1 |
	|       3 |    2 |
	|       3 |    3 |
	|       3 |    4 |
	|       3 |    5 |
	|       3 |    6 |
	|       3 |    0 |
	|       3 |    1 |
	|       3 |    2 |
	|       4 |    0 |
	|       5 |    0 |
	|       6 |    0 |
	|       6 |    0 |
	|       6 |    1 |
	|       6 |    2 |
	|       6 |    3 |
	|       6 |    4 |
	|       6 |    0 |
	|       6 |    0 |
	|       6 |    1 |
	|       6 |    2 |
	|       6 |    3 |
	|       6 |    4 |
	|       6 |    5 |
	|       6 |    6 |
	|       6 |    7 |
	|       6 |    8 |
	|       6 |    0 |
	|       6 |    1 |
	|       6 |    2 |
	|       6 |    3 |
	|       6 |    4 |
	|       6 |    5 |
	|       6 |    6 |
	|       6 |    7 |
	|       6 |    8 |
	|       7 |    0 |
	|       7 |    1 |
	|       7 |    2 |
	|       7 |    0 |
	|       7 |    1 |
	|       7 |    2 |
	|       7 |    3 |
	|       7 |    4 |
	|       7 |    0 |
	|       7 |    1 |
	|       7 |    2 |
	|       8 |    0 |
	|       8 |    1 |
	|       8 |    2 |
	|       8 |    3 |
	|       8 |    4 |
	|       8 |    5 |
	|       8 |    6 |
	|       8 |    0 |
	|       8 |    1 |
	|       8 |    2 |
	|       8 |    3 |
	|       8 |    4 |
	|       8 |    5 |
	|       8 |    6 |
	|       8 |    0 |
	|       8 |    1 |
	|       8 |    2 |
	|       8 |    3 |
	|       8 |    4 |
	|       8 |    5 |
	|       8 |    6 |
	|       8 |    7 |
	|       8 |    8 |
	|       8 |    0 |
	|       8 |    1 |
	|       8 |    2 |
	|       8 |    0 |
	|       8 |    1 |
	|       8 |    2 |
	|       8 |    3 |
	|       8 |    4 |
	|       8 |    5 |
	|       8 |    6 |
	|       8 |    7 |
	|       8 |    8 |
	|       8 |    0 |
	|       8 |    1 |
	|       8 |    2 |
	|       8 |    3 |
	|       8 |    4 |
	|       8 |    0 |
	|       8 |    1 |
	|       8 |    2 |
	|       8 |    3 |
	|       8 |    4 |
	|       8 |    5 |
	|       8 |    6 |
	|       8 |    7 |
	|       8 |    8 |
	|       9 |    0 |
	|       9 |    1 |
	|       9 |    2 |
	|       9 |    0 |
	|       9 |    1 |
	|       9 |    2 |
	|       9 |    3 |
	|       9 |    4 |
	|       9 |    5 |
	|       9 |    6 |
	|       9 |    0 |
	|      10 |    0 |
	|      10 |    0 |
	|      10 |    1 |
	|      10 |    2 |
	|      10 |    3 |
	|      10 |    4 |
	|      10 |    5 |
	|      10 |    6 |
	|      10 |    7 |
	|      10 |    8 |
	|      10 |    0 |
	|      10 |    1 |
	|      10 |    2 |
	|      10 |    3 |
	|      10 |    4 |
	|      10 |    5 |
	|      10 |    6 |
	|      10 |    0 |
	|      10 |    0 |
	|      10 |    1 |
	|      10 |    2 |
	|      10 |    0 |
	|      10 |    1 |
	|      10 |    2 |
	|      10 |    3 |
	|      10 |    4 |
	|      10 |    5 |
	|      10 |    6 |
	|      10 |    7 |
	|      10 |    8 |
	|      10 |    0 |
	|      10 |    1 |
	|      10 |    2 |
	|      10 |    3 |
	|      10 |    4 |
	|      10 |    0 |
	|      10 |    1 |
	|      10 |    2 |
	|      10 |    3 |
	|      10 |    4 |
	|      10 |    5 |
	|      10 |    6 |
	|      10 |    7 |
	|      10 |    8 |
	|      10 |    0 |
	|      10 |    1 |
	|      10 |    2 |
	|      11 |    0 |
	|      11 |    1 |
	|      11 |    2 |
	|      11 |    3 |
	|      11 |    4 |
	+---------+------+
	192 rows in set (0.00 sec)

	```

	```
	mysql>  SELECT * FROM  tv_shows;

	+----+-----------------------+
	| id | title                 |
	+----+-----------------------+
	|  2 | House                 |
	|  3 | Game of Thrones       |
	|  4 | The Big Bang Theory   |
	|  5 | New Girl              |
	|  6 | Silicon Valley        |
	|  7 | Breaking Bad          |
	|  8 | Better Call Saul      |
	|  9 | Dexter                |
	| 10 | Homeland              |
	| 11 | The Last Man on Earth |
	+----+-----------------------+
	10 rows in set (0.00 sec)

	mysql> 
	```
