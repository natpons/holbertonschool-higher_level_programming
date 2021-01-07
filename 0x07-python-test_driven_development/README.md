# 0x07. Python - Test-driven development

Foundations - Higher-level programming  Python

_by Guillaume, CTO at Holberton School_

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/246/giphy-4.gif)

## Background Context

### Important notice on intranet checks for Python projects

Starting from today:

-   Based on the requirements of each task,  **you should always write the documentation (module(s) + function(s)) and tests first**, before you actually code anything
-   The intranet checks for Python projects wont be released before their first deadline, in order for you to focus more on TDD and think about all possible cases
-   We strongly encourage you to work together on test cases, so that you dont miss any edge case.  **But not in the implementation of them!**
-   **Dont trust the user**, always think about all possible edge cases

## Resources

**Read or watch**:

-   [doctest  Test interactive Python examples](https://intranet.hbtn.io/rltoken/alaT1C9CeCbkRKh-yjMRww "doctest  Test interactive Python examples")  (_until 26.2.3.7. Warnings included_)
-   [doctest  Testing through documentation](https://intranet.hbtn.io/rltoken/cpEYbv_Z55QrSVRiuG5tUw "doctest  Testing through documentation")
-   [Unit Tests in Python](https://intranet.hbtn.io/rltoken/CELicn3K8hODQsWZak_h0g "Unit Tests in Python")

## Learning Objectives

At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/z8tHQfPZBZJOmguC5BeZ9Q "explain to anyone"),  **without the help of Google**:

### General

-   Why Python programming is awesome
-   Whats an interactive test
-   Why tests are important
-   How to write Docstrings to create tests
-   How to write documentation for each module and function
-   What are the basic option flags to create tests
-   How to find edge cases

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

### Python Test Cases

	-   Allowed editors:  `vi`,  `vim`,  `emacs`
	-   All your files should end with a new line
	-   All your test files should be inside a folder  `tests`
	-   All your test files should be text files (extension:  `.txt`)
	-   All your tests should be executed by using this command:  `python3 -m doctest ./tests/*`
												   -   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
												   -   All your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
												   -   A documentation is not a simple word, its a real sentence explaining whats the purpose of the module, class or method (the length of it will be verified)
												   -   We strongly encourage you to work together on test cases, so that you dont miss any edge case
