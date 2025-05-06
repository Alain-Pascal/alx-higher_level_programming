# 0x0A. Python - Inheritance

A repository about object oriented programming in the Python programming language

From the 0x0A. Python - Inheritance project at ALX-SE programme


## Resources

**Read or watch:**

* [Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
* [Multiple Inheritance](https://docs.python.org/3/tutorial/classes.html#multiple-inheritance)
* [Inheritance in Python](https://www.geeksforgeeks.org/inheritance-in-python/)
* [Learn to Program 10: Inheritance Magic Methods](https://www.youtube.com/watch?v=d8kCdLCi6Lk)

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
* All classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All functions (inside and outside a class) should have a documentation `(python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
* Have as many test cases as possible

### Documentation

* Do not use the words `import` or `from` inside comments, the checker will think you try to import some modules

## Mandatory Tasks

### 0. Lookup

Write a function that returns the list of available attributes and methods of an object:
* Prototype: `def lookup(obj):`
* Returns a `list` object
* Not allowed to import any module

```
user@ubuntu:~/0x0A$ cat 0-main.py
#!/usr/bin/python3
lookup = __import__('0-lookup').lookup

class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))

user@ubuntu:~/0x0A$ ./0-main.py
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'my_attr1', 'my_meth']
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
user@ubuntu:~/0x0A$
```

**Files:** [`0-lookup.py`](./0-lookup.py), [`0-main.py`](./mainFiles/0-main.py)

### 1. My list

Write a class `MyList` that inherits from `list:`
* Public instance method: `def print_sorted(self):` that prints the list, but sorted (ascending sort)
* You can assume that all the elements of the list will be of type `int`
* Not allowed to import any module

```
user@ubuntu:~/0x0A$ cat 1-main.py
#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)

user@ubuntu:~/0x0A$ ./1-main.py
[1, 4, 2, 3, 5]
[1, 2, 3, 4, 5]
[1, 4, 2, 3, 5]
user@ubuntu:~/0x0A$
```

**Files:** [`1-my_list.py`](./1-my_list.py), [`1-main.py`](./mainFiles/1-main.py), [`1-my_list.txt`](./tests/1-my_list.txt)

### 2. Exact same object

Write a function that returns `True` if the object is _exactly_ an instance of the specified class ; otherwise `False`.
* Prototype: `def is_same_class(obj, a_class):`
* Not allowed to import any module

```
user@ubuntu:~/0x0A$ cat 2-main.py
#!/usr/bin/python3
is_same_class = __import__('2-is_same_class').is_same_class

a = 1
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))
if is_same_class(a, float):
    print("{} is an instance of the class {}".format(a, float.__name__))
if is_same_class(a, object):
    print("{} is an instance of the class {}".format(a, object.__name__))

user@ubuntu:~/0x0A$ ./2-main.py
1 is an instance of the class int
user@ubuntu:~/0x0A$ 
```

**Files:**  [`2-is_same_class.py`](./2-is_same_class.py), [`2-main.py`](./mainFiles/2-main.py)

### 3. Same class or inherit from

Write a function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise `False`.
* Prototype: `def is_kind_of_class(obj, a_class):`
* Not allowed to import any module

```
user@ubuntu:~/0x0A$ cat 3-main.py
#!/usr/bin/python3
is_kind_of_class = __import__('3-is_kind_of_class').is_kind_of_class

a = 1
if is_kind_of_class(a, int):
    print("{} comes from {}".format(a, int.__name__))
if is_kind_of_class(a, float):
    print("{} comes from {}".format(a, float.__name__))
if is_kind_of_class(a, object):
    print("{} comes from {}".format(a, object.__name__))

user@ubuntu:~/0x0A$ ./3-main.py
1 comes from int
1 comes from object
user@ubuntu:~/0x0A$
```

**Files:** [`3-is_kind_of_class.py`](./3-is_kind_of_class.py), [`3-main.py`](./mainFiles/3-main.py)

### 4. Only sub class of

Write a function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise `False`.
* Prototype: `def inherits_from(obj, a_class):`
* Not allowed to import any module

```
user@ubuntu:~/0x0A$ cat 4-main.py
#!/usr/bin/python3
inherits_from = __import__('4-inherits_from').inherits_from

a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))

user@ubuntu:~/0x0A$ ./4-main.py
True inherited from class int
True inherited from class object
user@ubuntu:~/0x0A$
```

**Files:** [`4-inherits_from.py`](./4-inherits_from.py), [`4-main.py`](./mainFiles/4-main.py)

### 5. Geometry module

Write an empty class `BaseGeometry`.
* Not allowed to import any module

```
user@ubuntu:~/0x0A$ cat 5-main.py
#!/usr/bin/python3
BaseGeometry = __import__('5-base_geometry').BaseGeometry

bg = BaseGeometry()

print(bg)
print(dir(bg))
print(dir(BaseGeometry))

user@ubuntu:~/0x0A$ ./5-main.py
<5-base_geometry.BaseGeometry object at 0x7f2050c69208>
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
user@ubuntu:~/0x0A$
```

**Files:** [`5-base_geometry.py`](./5-base_geometry.py), [`5-main.py`](./mainFiles/5-main.py)

### 6. Improve Geometry

Write a class `BaseGeometry` (based on [`5-base_geometry.py`](./5-base_geometry.py)).
* Public instance method: `def area(self):` that raises an `Exception` with the message `area() is not implemented`
* Not allowed to import any module

```
user@ubuntu:~/0x0A$ cat 6-main.py
#!/usr/bin/python3
BaseGeometry = __import__('6-base_geometry').BaseGeometry

bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

user@ubuntu:~/0x0A$ ./6-main.py
[Exception] area() is not implemented
user@ubuntu:~/0x0A$ 
```

**Files:** [`6-base_geometry.py`](./6-base_geometry.py), [`6-main.py`](./mainFiles/6-main.py)

### 7. Integer validator

Write a class `BaseGeometry` (based on [`6-base_geometry.py`](./6-base_geometry.py)).
* Public instance method: `def area(self):` that raises an `Exception` with the message `area() is not implemented`
* Public instance method: `def integer_validator(self, name, value):` that validates `value`:
    * you can assume `name` is always a string
    * if `value` is not an integer: raise a `TypeError` exception, with the message `<name> must be an integer`
    * if `value` is less or equal to 0: raise a `ValueError` exception with the message `<name> must be greater than 0`
* Not allowed to import any module

```
user@ubuntu:~/0x0A$ cat 7-main.py
#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

bg = BaseGeometry()

bg.integer_validator("my_int", 12)
bg.integer_validator("width", 89)

try:
    bg.integer_validator("name", "John")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("age", 0)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("distance", -4)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

user@ubuntu:~/0x0A$ ./7-main.py
[TypeError] name must be an integer
[ValueError] age must be greater than 0
[ValueError] distance must be greater than 0
user@ubuntu:~/0x0A$
```

**Files:** [`7-base_geometry.py`](./7-base_geometry.py), [`7-main.py`](./mainFiles/7-main.py), [`7-base_geometry.txt`](./tests/7-base_geometry.txt)

### 8. Rectangle

Write a class `Rectangle` that inherits from BaseGeometry ([`7-base_geometry.py`](./7-base_geometry.py)).
* Instantiation with `width` and `height`: `def __init__(self, width, height):`
    * `width` and `height` must be private. No getter or setter
    * `width` and `height` must be positive integers, validated by `integer_validator`

```
user@ubuntu:~/0x0A$ cat 8-main.py
#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
print(dir(r))

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

user@ubuntu:~/0x0A$ ./8-main.py
<8-rectangle.Rectangle object at 0x7f6f488f7eb8>
['_Rectangle__height', '_Rectangle__width', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'area', 'integer_validator']
[AttributeError] 'Rectangle' object has no attribute 'width'
[TypeError] height must be an integer
user@ubuntu:~/0x0A$
```

**Files:** [`8-rectangle.py`](./8-rectangle.py), [`8-main.py`](./mainFiles/8-main.py)

### 9. Full rectangle

Write a class `Rectangle` that inherits from `BaseGeometry` ([`7-base_geometry.py`](./7-base_geometry.py)). (task based on [`8-rectangle.py`](./8-rectangle.py))
* Instantiation with `width` and `height`: `def __init__(self, width, height):`:
    * `width` and `height` must be private. No getter or setter
    * `width` and `height` must be positive integers validated by `integer_validator`
* the `area()` method must be implemented
* `print()` should print, and `str()` should return, the following rectangle description: `[Rectangle] <width>/<height>`

```
user@ubuntu:~/0x0A$ cat 9-main.py
#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
print(r.area())

user@ubuntu:~/0x0A$ ./9-main.py
[Rectangle] 3/5
15
user@ubuntu:~/0x0A$ 
```

**Files:** [`9-rectangle.py`](./9-rectangle.py), [`9-main.py`](./mainFiles/9-main.py)

### 10. Square #1



```

```

**Files:** [`10-square.py`](./10-square.py), [`10-main.py`](./mainFiles/10-main.py)

### 11. Square #2



```

```

**Files:** [`11-square.py`](./11-square.py), [`11-main.py`](./mainFiles/11-main.py)

## Optional Tasks

### 12. My integer



```

```

**Files:** [`100-my_int.py`](./100-my_int.py), [`100-main.py`](./mainFiles/11-main.py)

### 13. Can I?



```

```

**Files:** [`101-add_attribute.py`](./101-add_attribute.py), [`101-main.py`](./mainFiles/101-main.py)
