# 0x07. Python - Test-driven development

A repository about test-driven development in the Python programming language

From the 0x07. Python - Test-driven development project at ALX-SE programme

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
**Files:** [`0-add_integer.py`](./0-add_integer.py), [`0-add_integer.txt.test`](./tests/0-add_integer.txt), [`0-main.py`](./mainFiles/0-main.py)

### 1. Divide a matrix

Write a function that divides all elements of a matrix.

* Prototype: `def matrix_divided(matrix, div):`
* `matrix` must be a list of lists of integers or floats, otherwise raise a `TypeError` exception with the message `matrix must be a matrix (list of lists) of integers/floats`
* Each row of the `matrix` must be of the same size, otherwise raise a `TypeError` exception with the message `Each row of the matrix must have the same size`
* `div` must be a number (integer or float), otherwise raise a `TypeError` exception with the message `div must be a number`
* `div` can’t be equal to `0`, otherwise raise a `ZeroDivisionError` exception with the message `division by zero`
* All elements of the matrix should be divided by `div`, rounded to 2 decimal places
* Returns a new matrix
* Not allowed to import any module
```
user@ubuntu:~/0x07$ cat 2-main.py
#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)

user@ubuntu:~/0x07$ ./2-main.py
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
[[1, 2, 3], [4, 5, 6]]
user@ubuntu:~/0x07$ python3 -m doctest -v ./tests/2-matrix_divided.txt | tail -2
5 passed and 0 failed.
Test passed.
user@ubuntu:~/0x07$ 
```
Note: Tests should cover all possible cases.

**Files:** [`2-matrix_divided.py`](./2-matrix_divided.py), [`2-matrix_divided.txt.test`](./tests/2-matrix_divided.txt), [`2-main.py`](./mainFiles/2-main.py)

### 2. Say my name

Write a function that prints `My name is <first name> <last name>`.

* Prototype: `def say_my_name(first_name, last_name=""):`
* `first_name` and `last_name` must be strings, otherwise raise a `TypeError` exception with the message `first_name must be a string` or `last_name must be a string`
* Not allowed to import any module

```
user@ubuntu:~/0x07$ cat 3-main.py
#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("John", "Smith")
say_my_name("Walter", "White")
say_my_name("Bob")
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)

user@ubuntu:~/0x07$ ./3-main.py | cat -e
My name is John Smith$
My name is Walter White$
My name is Bob $
first_name must be a string$
user@ubuntu:~/0x07$ python3 -m doctest -v ./tests/3-say_my_name.txt | tail -2
5 passed and 0 failed.
Test passed.
user@ubuntu:~/0x07$
```

Note: Tests should cover all possible cases.

**Files:** [`3-say_my_name.py`](./3-say_my_name.py), [`3-say_my_name.txt.test`](./tests/3-say_my_name.txt), [`3-main.py`](./mainFiles/3-main.py)

### 3. Print square

Write a function that prints a square with the character #.

* Prototype: `def print_square(size):`
* `size` is the size length of the square
* `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
* if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
* if `size` is a float and is less than 0, raise a `TypeError` exception with the message `size must be an integer`
* Not allowed to import any module

```
user@ubuntu:~/0x07$ cat 4-main.py
#!/usr/bin/python3
print_square = __import__('4-print_square').print_square

print_square(4)
print("")
print_square(10)
print("")
print_square(0)
print("")
print_square(1)
print("")
try:
    print_square(-1)
except Exception as e:
    print(e)
print("")

user@ubuntu:~/0x07$ ./4-main.py
####
####
####
####

##########
##########
##########
##########
##########
##########
##########
##########
##########
##########


#

size must be >= 0

user@ubuntu:~/0x07$ python3 -m doctest -v ./tests/4-print_square.txt
user@ubuntu:~/0x07$
```

**Files:** [`4-print_square.py`](./4-print_square.py), [`4-print_square.txt.test`](./tests/4-print_square.txt), [`4-main.py`](./mainFiles/4-main.py)

### 4. Text indentation

Write a function that prints a text with 2 new lines after each of these characters: `.`, `?` and `:`

* Prototype: `def text_indentation(text):`
* `text` must be a string, otherwise raise a `TypeError` exception with the message `text must be a string`
* There should be no space at the beginning or at the end of each printed line
* Not allowed to import any module
```
user@ubuntu:~/0x07$ cat 5-main.py
#!/usr/bin/python3
text_indentation = __import__('5-text_indentation').text_indentation

text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")

user@ubuntu:~/0x07$ ./5-main.py | cat -e
Lorem ipsum dolor sit amet, consectetur adipiscing elit.$
$
Quonam modo?$
$
Utrum igitur tibi litteram videor an totas paginas commovere?$
$
Non autem hoc:$
$
igitur ne illud quidem.$
$
Fortasse id optimum, sed ubi illud:$
$
Plus semper voluptatis?$
$
Teneo, inquit, finem illi videri nihil dolere.$
$
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum rationi oboediens.$
$
Si id dicis, vicimus.$
$
Inde sermone vario sex illa a Dipylo stadia confecimus.$
$
Sin aliud quid voles, postea.$
$
Quae animi affectio suum cuique tribuens atque hanc, quam dico.$
$
Utinam quidem dicerent alium alio beatiorem! Iam ruinas videresuser@ubuntu:~/0x07$
user@ubuntu:~/0x07$ python3 -m doctest -v ./tests/5-text_indentation.txt
user@ubuntu:~/0x07$
```

**Files:** [`5-text_indentation.py`](./5-text_indentation.py), [`5-text_indentation.txt.test`](./tests/5-text_indentation.txt), [`5-main.py`](./mainFiles/5-main.py)

### 5. Max integer - Unittest

Since the beginning you have been creating “Interactive tests”. For this exercise, you will add Unittests.

In this task, you will write unittests for the function `def max_integer(list=[]):`.

* Test file should be inside a folder tests
* Use the [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
* Test file should be python files (extension: `.py`)
* Test file should be executed by using this command: `python3 -m unittest tests.6-max_integer_test`
* All tests must be passable by the function below
* Test many cases as possible
```
user@ubuntu:~/0x07$ cat 6-max_integer.py
#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result

user@ubuntu:~/0x07$ 
user@ubuntu:~/0x07$ cat 6-main.py
#!/usr/bin/python3
max_integer = __import__('6-max_integer').max_integer

print(max_integer([1, 2, 3, 4]))
print(max_integer([1, 3, 4, 2]))
user@ubuntu:~/0x07$
user@ubuntu:~/0x07$ ./6-main.py
4
4
user@ubuntu:~/0x07$
user@ubuntu:~/0x07$ python3 -m unittest tests.6-max_integer_test 2>&1 | tail -1
OK
user@ubuntu:~/0x07$
user@ubuntu:~/0x07$ head -7 tests/6-max_integer_test.py 
#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
user@ubuntu:~/0x07$
```

**Files:** [`6-max_integer.py`](./6-max_integer.py), [`6-max_integer_test.py`](./tests/6-max_integer_test.py), [`6-main.py`](./mainFiles/6-main.py)

## Optional Tasks

### 6. Matrix multiplication

Write a function that multiplies 2 matrices:

* Read: [Matrix multiplication - only Matrix product (two matrices)](https://en.wikipedia.org/wiki/Matrix_multiplication)
* Prototype: `def matrix_mul(m_a, m_b):`
* `m_a` and `m_b` must be validated with these requirements in this order
* `m_a` and `m_b` must be an list of lists of integers or floats:

    * if `m_a` or `m_b` is not a list: raise a `TypeError` exception with the message `m_a must be a list` or `m_b must be a list`
    * if `m_a` or `m_b` is not a list of lists: raise a `TypeError` exception with the message `m_a must be a list of lists` or `m_b must be a list of lists`
    * if `m_a` or `m_b` is empty (it means: `= []` or `= [[]`]): raise a `ValueError` exception with the message `m_a can't be empty` or `m_b can't be empty`
    * if one element of those list of lists is not an integer or a float: raise a `TypeError` exception with the message `m_a should contain only integers or floats` or `m_b should contain only integers or floats`
    * if `m_a` or `m_b` is not a rectangle (all ‘rows’ should be of the same size): raise a `TypeError` exception with the message `each row of m_a must be of the same size` or `each row of m_b must be of the same size`
* If `m_a` and `m_b` can’t be multiplied: raise a `ValueError` exception with the message `m_a and m_b can't be multiplied`
* Not allowed to import any module
```
user@ubuntu:~/0x07$ cat 100-main.py
#!/usr/bin/python3
matrix_mul = __import__('100-matrix_mul').matrix_mul

print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))

user@ubuntu:~/0x07$ ./100-main.py 
[[7, 10], [15, 22]]
[[13, 16]]
user@ubuntu:~/0x07$ python3 -m doctest -v ./tests/100-matrix_mul.txt | tail -2
6 passed and 0 failed.
Test passed.
user@ubuntu:~/0x07$
```

**Files:** [`100-matrix_mul.py`](./100-matrix_mul.py), [`100-matrix_mul.txt.test`](./tests/100-matrix_mul.txt), [`100-main.py`](./mainFiles/100-main.py)

### 7. Lazy matrix multiplication

Write a function that multiplies 2 matrices by using the module [NumPy](https://numpy.org/doc/stable/)

To install it: `pip3 install numpy==1.15.0`

* Prototype: `def lazy_matrix_mul(m_a, m_b):`
* Test cases should be the same as `100-matrix_mul` but with new exception type/message
```
user@ubuntu:~/0x07$ cat 101-main.py
#!/usr/bin/python3
lazy_matrix_mul = __import__('101-lazy_matrix_mul').lazy_matrix_mul

print(lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]]))

user@ubuntu:~/0x07$ ./101-main.py 
[[ 7 10]
 [15 22]]
[[13 16]]
user@ubuntu:~/0x07$ python3 -m doctest -v ./tests/101-lazy_matrix_mul.txt 
user@ubuntu:~/0x07$ 
```

**Files:** [`101-lazy_matrix_mul.py`](./101-lazy_matrix_mul.py), [`101-lazy_matrix_mul.txt.test`](./tests/101-lazy_matrix_mul.txt), [`101-main.py`](./mainFiles/101-main.py)

### 8. CPython #3: Python Strings

Create a function that prints Python strings.

* Prototype: `void print_python_string(PyObject *p);`
* Format: see example
* If `p` is not a valid string, print an error message (see example)
* Read: [Unicode HOWTO](https://docs.python.org/3.4/howto/unicode.html)

About:

* Python version: 3.4
* Use the C standard library
* Shared library will be compiled with this command line: `gcc -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 102-python.c`
```
user@ubuntu:~/0x07. Pyhton Strings$ cat 102-tests.py
import ctypes

lib = ctypes.CDLL('./libPython.so')
lib.print_python_string.argtypes = [ctypes.py_object]
s = "The spoon does not exist"
lib.print_python_string(s)
s = "ложка не существует"
lib.print_python_string(s)
s = "La cuillère n'existe pas"
lib.print_python_string(s)
s = "勺子不存在"
lib.print_python_string(s)
s = "숟가락은 존재하지 않는다."
lib.print_python_string(s)
s = "スプーンは存在しない"
lib.print_python_string(s)
s = b"The spoon does not exist"
lib.print_python_string(s)
user@ubuntu:~/0x07. Pyhton Strings$ gcc -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 102-python.c
user@ubuntu:~/0x07. Pyhton Strings$ python3 ./102-tests.py
[.] string object info
  type: compact ascii
  length: 24
  value: The spoon does not exist
[.] string object info
  type: compact unicode object
  length: 19
  value: ложка не существует
[.] string object info
  type: compact unicode object
  length: 24
  value: La cuillère n'existe pas
[.] string object info
  type: compact unicode object
  length: 5
  value: 勺子不存在
[.] string object info
  type: compact unicode object
  length: 14
  value: 숟가락은 존재하지 않는다.
[.] string object info
  type: compact unicode object
  length: 10
  value: スプーンは存在しない
[.] string object info
  [ERROR] Invalid String Object
user@ubuntu:~/0x07. Pyhton Strings$
```

**Files:** [`102-python.c`](./102-python.c), [`102-tests.py`](./tests/102-tests.py)
