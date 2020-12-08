# 0x01. Python - if/else, loops, functions

Foundations - Higher-level programming  Python

_by Guillaume, CTO at Holberton School_

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/233/code.png)

## Resources

**Read or watch**:

-   [More Control Flow Tools](https://intranet.hbtn.io/rltoken/R7uTXYVOjUilq6rCjsQcFg "More Control Flow Tools")  (_Read until 4.6. Defining Functions included_)
-   [Myths about Indentation](https://intranet.hbtn.io/rltoken/Y-HaMMJBKPseiVDo_v9PVg "Myths about Indentation")
-   [IndentationError](https://intranet.hbtn.io/rltoken/AorC2VSZ4yCOx-AbatvKLA "IndentationError")
-   [How To Use String Formatters in Python 3](https://intranet.hbtn.io/rltoken/arGQeiwUbFn3JOoYpw84yA "How To Use String Formatters in Python 3")
-   [Learn to Program](https://intranet.hbtn.io/rltoken/mlo-dauC8pSM_NrO5VYobw "Learn to Program")
-   [Learn to Program 2 : Looping](https://intranet.hbtn.io/rltoken/mlo-dauC8pSM_NrO5VYobw "Learn to Program 2 : Looping")
-   [PEP 8  Style Guide for Python Code](https://intranet.hbtn.io/rltoken/mq1IFaMhqpk2IHE0dC6UuQ "PEP 8 -- Style Guide for Python Code")

**man or help**:

-   `python3`

## Learning Objectives

At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/UX0jIrVINsbuomDsYv4a1w "explain to anyone"),  **without the help of Google**:

### General

-   Why Python programming is awesome
-   Why indentation is so important in Python
-   How to use the  `if`,  `if ... else`  statements
-   How to use comments
-   How to affect values to variables
-   How to use the  `while`  and  `for`  loops
-   How is Pythons  `for`  different from  `C`s?
-   How to use the  `break`  and  `continues`  statements
-   How to use  `else`  clauses on loops
-   What does the  `pass`  statement do, and when to use it
-   How to use  `range`
-   What is a function and how do you use functions
-   What does return a function that does not use any  `return`  statement
-   Scope of variables
-   Whats a traceback
-   What are the arithmetic operators and how to use them

## Requirements

### Python Scripts

-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files will be interpreted/compiled on Ubuntu 14.04 LTS using  `python3`  (version 3.4.3)
	-   All your files should end with a new line
	-   The first line of all your files should be exactly  `#!/usr/bin/python3`
	-   A  `README.md`  file, at the root of the folder of the project, is mandatory
	-   Your code should use the  `PEP 8`  style (version 1.7.*)
	-   All your files must be executable
	-   The length of your files will be tested using  `wc`

### C Scripts

	-   Allowed editors:  `vi`,  `vim`,  `emacs`
	-   All your files will be compiled on Ubuntu 14.04 LTS
	-   Your programs and functions will be compiled with  `gcc 4.8.4`  using the flags  `-Wall`  `-Werror`  `-Wextra`  `and -pedantic`
	-   All your files should end with a new line
	-   Your code should use the  `Betty`  style. It will be checked using  [betty-style.pl](https://github.com/holbertonschool/Betty/blob/master/betty-style.pl "betty-style.pl")  and  [betty-doc.pl](https://github.com/holbertonschool/Betty/blob/master/betty-doc.pl "betty-doc.pl")
	-   You are not allowed to use global variables
	-   No more than 5 functions per file
	-   In the following examples, the  `main.c`  files are shown as examples. You can use them to test your functions, but you dont have to push them to your repo (if you do we wont take them into account). We will use our own  `main.c`  files at compilation. Our  `main.c`  files might be different from the one shown in the examples
	-   The prototypes of all your functions should be included in your header file called  `lists.h`
	-   Dont forget to push your header file
	-   All your header files should be include guarded# 0x01. Python - if/else, loops, functions

	Foundations - Higher-level programming  Python

	_by Guillaume, CTO at Holberton School_

	![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/233/code.png)

## Resources

	**Read or watch**:

	-   [More Control Flow Tools](https://intranet.hbtn.io/rltoken/R7uTXYVOjUilq6rCjsQcFg "More Control Flow Tools")  (_Read until 4.6. Defining Functions included_)
	-   [Myths about Indentation](https://intranet.hbtn.io/rltoken/Y-HaMMJBKPseiVDo_v9PVg "Myths about Indentation")
	-   [IndentationError](https://intranet.hbtn.io/rltoken/AorC2VSZ4yCOx-AbatvKLA "IndentationError")
	-   [How To Use String Formatters in Python 3](https://intranet.hbtn.io/rltoken/arGQeiwUbFn3JOoYpw84yA "How To Use String Formatters in Python 3")
	-   [Learn to Program](https://intranet.hbtn.io/rltoken/mlo-dauC8pSM_NrO5VYobw "Learn to Program")
	-   [Learn to Program 2 : Looping](https://intranet.hbtn.io/rltoken/mlo-dauC8pSM_NrO5VYobw "Learn to Program 2 : Looping")
	-   [PEP 8  Style Guide for Python Code](https://intranet.hbtn.io/rltoken/mq1IFaMhqpk2IHE0dC6UuQ "PEP 8 -- Style Guide for Python Code")

	**man or help**:

	-   `python3`

## Learning Objectives

	At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/UX0jIrVINsbuomDsYv4a1w "explain to anyone"),  **without the help of Google**:

### General

	-   Why Python programming is awesome
	-   Why indentation is so important in Python
	-   How to use the  `if`,  `if ... else`  statements
	-   How to use comments
	-   How to affect values to variables
	-   How to use the  `while`  and  `for`  loops
	-   How is Pythons  `for`  different from  `C`s?
	-   How to use the  `break`  and  `continues`  statements
	-   How to use  `else`  clauses on loops
	-   What does the  `pass`  statement do, and when to use it
	-   How to use  `range`
	-   What is a function and how do you use functions
	-   What does return a function that does not use any  `return`  statement
	-   Scope of variables
	-   Whats a traceback
	-   What are the arithmetic operators and how to use them

## Requirements

### Python Scripts

	-   Allowed editors:  `vi`,  `vim`,  `emacs`
	-   All your files will be interpreted/compiled on Ubuntu 14.04 LTS using  `python3`  (version 3.4.3)
	-   All your files should end with a new line
	-   The first line of all your files should be exactly  `#!/usr/bin/python3`
	-   A  `README.md`  file, at the root of the folder of the project, is mandatory
	-   Your code should use the  `PEP 8`  style (version 1.7.*)
	-   All your files must be executable
	-   The length of your files will be tested using  `wc`

### C Scripts

	-   Allowed editors:  `vi`,  `vim`,  `emacs`
	-   All your files will be compiled on Ubuntu 14.04 LTS
	-   Your programs and functions will be compiled with  `gcc 4.8.4`  using the flags  `-Wall`  `-Werror`  `-Wextra`  `and -pedantic`
	-   All your files should end with a new line
	-   Your code should use the  `Betty`  style. It will be checked using  [betty-style.pl](https://github.com/holbertonschool/Betty/blob/master/betty-style.pl "betty-style.pl")  and  [betty-doc.pl](https://github.com/holbertonschool/Betty/blob/master/betty-doc.pl "betty-doc.pl")
	-   You are not allowed to use global variables
	-   No more than 5 functions per file
	-   In the following examples, the  `main.c`  files are shown as examples. You can use them to test your functions, but you dont have to push them to your repo (if you do we wont take them into account). We will use our own  `main.c`  files at compilation. Our  `main.c`  files might be different from the one shown in the examples
	-   The prototypes of all your functions should be included in your header file called  `lists.h`
	-   Dont forget to push your header file
	-   All your header files should be include guarded
