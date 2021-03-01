
# 0x0D. SQL - Introduction

-   Foundations - Higher-level programming  Databases

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/rtcwz.jpg)

## Resources

**Read or watch**:

-   [What is Database & SQL?](https://intranet.hbtn.io/rltoken/khEqMKp1PHvKpfO18d4fLQ "What is Database & SQL?")
-   [A Basic MySQL Tutorial](https://intranet.hbtn.io/rltoken/qrONF5FZPsRxRJ2FkLVPcg "A Basic MySQL Tutorial")
-   [Basic SQL statements: DDL and DML](https://intranet.hbtn.io/rltoken/ibCYnC9CDgZg5NQQvccBWw "Basic SQL statements: DDL and DML")  (_no need to read the chapter Privileges_)
-   [Basic queries: SQL and RA](https://intranet.hbtn.io/rltoken/yelYhpf7l0FcRIPCVfnMLw "Basic queries: SQL and RA")
-   [SQL technique: functions](https://intranet.hbtn.io/rltoken/3aQcovOE-clrD8yIfxFE9Q "SQL technique: functions")
-   [SQL technique: subqueries](https://intranet.hbtn.io/rltoken/lTXnq6pdk59x2h_Y-q0-Hg "SQL technique: subqueries")
-   [What makes the big difference between a backtick and an apostrophe?](https://intranet.hbtn.io/rltoken/R--kAkehyaawZFY4m1inxQ "What makes the big difference between a backtick and an apostrophe?")
-   [MySQL Cheat Sheet](https://intranet.hbtn.io/rltoken/aGZu7ulJpbbKcDhcz49yrg "MySQL Cheat Sheet")
-   [MySQL 5.7 SQL Statement Syntax](https://intranet.hbtn.io/rltoken/XrqR4oh6zsk0eOKoTgkA3Q "MySQL 5.7 SQL Statement Syntax")

## Learning Objectives

At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/fc2coosqJh9IxKyYgnDsrg "explain to anyone"),  **without the help of Google**:

### General

-   Whats a database
-   Whats a relational database
-   What does SQL stand for
-   Whats MySQL
-   How to create a database in MySQL
-   What does  `DDL`  and  `DML`  stand for
-   How to  `CREATE`  or  `ALTER`  a table
-   How to  `SELECT`  data from a table
-   How to  `INSERT`,  `UPDATE`  or  `DELETE`  data
-   What are  `subqueries`
-   How to use MySQL functions

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


	```

### Install MySQL 5.7 on Ubuntu 14.04 LTS

```
$ echo 'deb http://repo.mysql.com/apt/ubuntu/ trusty mysql-5.7-dmr' | sudo tee -a /etc/apt/sources.list
$ sudo apt-get update
$ sudo apt-get install mysql-server-5.7
...
$ mysql --version
mysql  Ver 14.14 Distrib 5.7.8-rc, for Linux (x86_64) using  EditLine wrapper


```

**Dont forget your  `root`  password**

Connect to your MySQL server:

```
$ mysql -hlocalhost -uroot -p
Password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 42
Server version: 5.7.8-rc MySQL Community Server (GPL)

Copyright (c) 2000, 2016, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> 
mysql> quit
Bye


	```

	If you have some issues to upgrade to 5.7, dont hesitate to cleanup your server of any MySQL packages:  `sudo apt-get remove --purge mysql-server mysql-client mysql-common`

### Use container-on-demand to run MySQL

-   Ask for container  `Ubuntu 14.04 - Python 3.4`
-   Connect via SSH
-   OR connect via the Web terminal
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


```

**In the container, credentials are  `root/root`**
