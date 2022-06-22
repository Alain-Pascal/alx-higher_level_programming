# 0x06-python-classes

A repository about object oriented programming in the Python programming language

From the 0x06. Python - Classes and Objects project at ALX-SE programme

## Background Context

OOP is a totally new concept for all of you (especially those who think they know about it :)). It’s VERY important that you read at least all the material that is listed bellow (and skip what we recommend you to skip, you will see them later in the curriculum).

As usual, make sure you type (never copy and paste), test, understand all examples shown in the following links (including those in the video), test again etc. The biggest and most important takeaway of this project is: experiment by yourself OOP, play with it!

Read or watch the below resources in the order presented.

## Resources

* [Object Oriented Programming](https://python.swaroopch.com/oop.html) (*Read everything until the paragraph “Inheritance” excluded. You do NOT have to learn about class attributes, `classmethod` and `staticmethod` yet*)
* [Object Oriented Programming](https://python-course.eu/oop/object-oriented-programming.php) (*Please **be careful**: in most of the following paragraphs, the author shows things the way you should not use or write a class in order to help you better understand some concepts and how everything works in Python 3. Make sure you read everything in the following paragraphs: General Introduction, First-class Everything, A Minimal Class in Python, Attributes (You DON’T have to learn about class attributes), Methods, The `__init__` Method, “Data Abstraction, Data Encapsulation, and Information Hiding,” “Public, Protected, and Private Attributes”*)
* [Properties vs. Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php)
* [Learn Python 9: Object Oriented Programming](https://www.youtube.com/watch?v=1AGyBuVCTeE)
* [Python Classes and Objects](https://www.youtube.com/watch?v=apACNr7DC_s)
* [Object Oriented Programming](https://www.youtube.com/watch?v=-DP1i2ZU9gk)

## Requirements

### General

* Allowed editors: `vi`, `vim`, `emacs`
* All files will be compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All files should end with a new line
* The first line of all files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project is mandatory
* Code should use the pycodestyle (version `2.8.*`)
* All files must be executable
* The length of files will be tested using `wc`
* All modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All functions (inside and outside a class) should have a documenation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
* A documentation is not a simple word, it is a real sentence explaining what is the purpose of the module, class or method (the length of it will be verified)

## More Info

**Documentation is now mandatory!** Each module, class, and method must contain docstring as comments. [Example Google Style Python Docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)

## Mandatory Tasks

### 0. My first square



### 1. Square with size



### 2. Size validation



### 3. Area of a square



### 4. Access and update private attribute



### 5. Printing a square



### 6. Coordinates of a square



## Optional Tasks

### 7. Singly linked list



### 8. Print Square instance



### 9. Compare 2 squares



### 10. ByteCode -> Python #5

Write the Python class MagicClass that does exactly the same as the following Python bytecode:

```
Disassembly of __init__:
 10           0 LOAD_CONST               1 (0)
              3 LOAD_FAST                0 (self)
              6 STORE_ATTR               0 (_MagicClass__radius)

 11           9 LOAD_GLOBAL              1 (type)
             12 LOAD_FAST                1 (radius)
             15 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             18 LOAD_GLOBAL              2 (int)
             21 COMPARE_OP               9 (is not)
             24 POP_JUMP_IF_FALSE       60
             27 LOAD_GLOBAL              1 (type)
             30 LOAD_FAST                1 (radius)
             33 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             36 LOAD_GLOBAL              3 (float)
             39 COMPARE_OP               9 (is not)
             42 POP_JUMP_IF_FALSE       60

 12          45 LOAD_GLOBAL              4 (TypeError)
             48 LOAD_CONST               2 ('radius must be a number')
             51 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             54 RAISE_VARARGS            1
             57 JUMP_FORWARD             0 (to 60)

 13     >>   60 LOAD_FAST                1 (radius)
             63 LOAD_FAST                0 (self)
             66 STORE_ATTR               0 (_MagicClass__radius)
             69 LOAD_CONST               3 (None)
             72 RETURN_VALUE

Disassembly of area:
 17           0 LOAD_FAST                0 (self)
              3 LOAD_ATTR                0 (_MagicClass__radius)
              6 LOAD_CONST               1 (2)
              9 BINARY_POWER
             10 LOAD_GLOBAL              1 (math)
             13 LOAD_ATTR                2 (pi)
             16 BINARY_MULTIPLY
             17 RETURN_VALUE

Disassembly of circumference:
 21           0 LOAD_CONST               1 (2)
              3 LOAD_GLOBAL              0 (math)
              6 LOAD_ATTR                1 (pi)
              9 BINARY_MULTIPLY
             10 LOAD_FAST                0 (self)
             13 LOAD_ATTR                2 (_MagicClass__radius)
             16 BINARY_MULTIPLY
             17 RETURN_VALUE
```

* Tip: [Python bytecode](https://docs.python.org/3.4/library/dis.html)
