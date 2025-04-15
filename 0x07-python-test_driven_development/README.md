# 0x07. Python - Test-driven development

A repository about object oriented programming in the Python programming language

From the 00x07. Python - Test-driven development project at ALX-SE programme

## Concepts

Take a look at this concept:

[Never forget a test](./Never_forget_a_test.md)


## Resources

**Read or watch:**

* [doctest - Test interactive Python examples](https://docs.python.org/3.4/library/doctest.html) (_until "26.2.3.7. Warning" included_)
* [doctest - Testing through documentation](https://pymotw.com/3/doctest/)
* [Unit Tests in Python](https://www.youtube.com/watch?v=1Lfv5tUGsn8)
* [Unit test module](https://www.youtube.com/watch?v=6tNS--WetLI)
* [Interactive and Non-interactive tests](https://mattermost.com/blog/testing-python-understanding-doctest-and-unittest/)

## Requirements

### Python Scripts

* Allowed editors: `vi`, `vim`, `emacs`
* All files will be compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All files should end with a new line
* The first line of all files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project is mandatory
* Code should use the pycodestyle (version `2.8.*`)
* All files must be executable
* The length of files will be tested using `wc`

### Python Test Cases

* Allowed editors: `vi`, `vim`, `emacs`
* All files should end with a new line
* All test files should be inside a folder `tests`
* All test files should be text files (extension: `.txt`)
* All tests should be executed by using this command: `python3 -m doctest ./tests/*`
* All modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Mandatory Tasks

### 0. Integers addition

Write a function that adds 2 integers.
  * Prototype: `def add_integer(a, b=98):`
  * `a` and `b` must be integers or floats, otherwise raise a `TypeError` exception with the message `a must be an integer` or `b must be an integer`
  * `a` and `b` must be first casted to integers if they are float
  * Returns an integer: the addition of `a` and `b`
  * Not allowed to import any module
```
user@ubuntu:~/0x07$ cat 0-main.py
#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)

user@ubuntu:~/0x07$ ./0-main.py
3
98
100
98
b must be an integer
a must be an integer
user@ubuntu:~/0x07$ python3 -m doctest -v ./tests/0-add_integer.txt | tail -2
9 passed and 0 failed.
Test passed.
user@ubuntu:~/0x07$ python3 -c 'print(__import__("0-add_integer").__doc__)' | wc -l
5
user@ubuntu:~/0x07$ python3 -c 'print(__import__("0-add_integer").add_integer.__doc__)' | wc -l
3
user@ubuntu:~/0x07$ 
```

### 1. SDivide a matrix



### 2. Say my name



### 3. Print square



### 4. Text indentation



### 5. Max integer - Unittest



## Optional Tasks

### 6. Matrix multiplication



### 7. Lazy matrix multiplication



### 8. CPython #3: Python Strings


