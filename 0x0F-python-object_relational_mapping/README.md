# 0x0F. Python - Object-relational mapping

## Before you start

**Please make sure your MySQL server is in 5.7**  ->  [How to install MySQL 5.7 in Ubuntu 14.04](https://intranet.hbtn.io/rltoken/mqTU28SAIfz_-9w7rZipMw "How to install MySQL 5.7 in Ubuntu 14.04")

## Background Context

In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module  `MySQLdb`  to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module  `SQLAlchemy`  (dont ask me how to pronounce it) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be What can I do with my objects and not How this object is stored? where? when?. You wont write any SQL queries only Python code. Last thing, your code wont be storage type dependent. You will be able to change your storage easily without re-writing your entire project.

Without ORM:

```
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()

```

With an ORM:

```
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
print("{}: {}".format(state.id, state.name))
session.close()

```

Do you see the difference? Cool, right?

The biggest difficulty with ORM is: The syntax!

Indeed, all of them have the same type of syntax, but not always. Please read tutorials and dont read the entire documentation before starting, just jump on it if you dont get something.

## Resources

**Read or watch**:

-   [Object-relational mappers](https://intranet.hbtn.io/rltoken/IqdjUaZ31ZfP6eT-lTyUkA "Object-relational mappers")
-   [mysqlclient/MySQLdb documentation](https://intranet.hbtn.io/rltoken/rMJpVJ1_YjMWfvY00I7Kpw "mysqlclient/MySQLdb documentation")  (_please dont pay attention to  `_mysql`_)
-   [MySQLdb tutorial](https://intranet.hbtn.io/rltoken/DJz5W6Y13-6qUSTPTGrHYw "MySQLdb tutorial")
-   [SQLAlchemy tutorial](https://intranet.hbtn.io/rltoken/9JWveMwNKe3IUErdEbDsUQ "SQLAlchemy tutorial")
-   [SQLAlchemy](https://intranet.hbtn.io/rltoken/E9dLS6Shaezq4ivnGxN_RA "SQLAlchemy")
-   [mysqlclient/MySQLdb](https://intranet.hbtn.io/rltoken/QFgtVxz2w-C1y1OB8uls1g "mysqlclient/MySQLdb")
-   [Introduction to SQLAlchemy](https://intranet.hbtn.io/rltoken/I5bvhPGTOu3_-T-4jpN-hg "Introduction to SQLAlchemy")
-   [Flask SQLAlchemy](https://intranet.hbtn.io/rltoken/UvaHESHeqlRA0Z0uQFi0_A "Flask SQLAlchemy")
-   [10 common stumbling blocks for SQLAlchemy newbies](https://intranet.hbtn.io/rltoken/Zb8Yc2WycLLYX8gnLlwZKw "10 common stumbling blocks for SQLAlchemy newbies")
-   [Python SQLAlchemy Cheatsheet](https://intranet.hbtn.io/rltoken/XHPAX7-ydSou2BLWHII8Vw "Python SQLAlchemy Cheatsheet")
-   [SQLAlchemy ORM Tutorial for Python Developers](https://intranet.hbtn.io/rltoken/aeLSQ039BhLhamU2BjqsOw "SQLAlchemy ORM Tutorial for Python Developers")  (_**Warning:**  This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL_)
-   [SQLAlchemy Tutorial](https://intranet.hbtn.io/rltoken/cmfi9C_nRXrmnwaJfCPyxA "SQLAlchemy Tutorial")

## Learning Objectives

At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/pAhQMOZ5dg4WaUDzqIwp7A "explain to anyone"),  **without the help of Google**:

### General

-   Why Python programming is awesome
-   How to connect to a MySQL database from a Python script
-   How to  `SELECT`  rows in a MySQL table from a Python script
-   How to  `INSERT`  rows in a MySQL table from a Python script
-   What ORM means
-   How to map a Python Class to a MySQL table

## Requirements

### General

-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files will be interpreted/compiled on Ubuntu 14.04 LTS using  `python3`  (version 3.4.3)
-   Your files will be executed with  `MySQLdb`  version  `1.3.x`
-   Your files will be executed with  `SQLAlchemy`  version  `1.2.x`
-   All your files should end with a new line
-   The first line of all your files should be exactly  `#!/usr/bin/python3`
-   A  `README.md`  file, at the root of the folder of the project, is mandatory
-   Your code should use the  `PEP 8`  style (`version 1.7.*`)
-   All your files must be executable
-   The length of your files will be tested using  `wc`
-   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
-   All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
-   All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`  and  `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
-   A documentation is not a simple word, its a real sentence explaining whats the purpose of the module, class or method (the length of it will be verified)
-   You are not allowed to use  `execute`  with sqlalchemy

## More Info

### Install  `MySQLdb`  module version  `1.3.x`

For installing  `MySQLdb`, you need to have  `MySQL`  installed:  [How to install MySQL 5.7 in Ubuntu 14.04](https://intranet.hbtn.io/rltoken/mqTU28SAIfz_-9w7rZipMw "How to install MySQL 5.7 in Ubuntu 14.04")

```
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient==1.3.10
...
$ python3
>>> import MySQLdb
>>> MySQLdb.__version__ 
'1.3.10'

```

### Install  `SQLAlchemy`  module version  `1.2.x`

```
$ pip3 install SQLAlchemy==1.2.5
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.2.5'

```

Also, you can have this warning message:

```
/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be re
moved in a future release.")                                                                                                                   
cursor.execute(statement, parameters)  
```
You can ignore it.
