# 0x09. Python - Everything is object

A repository about object oriented programming in the Python programming language

From the 0x09. Python - Everything is object project at ALX-SE programme

## Background Context

Now that we understand that everything is an object and have a little bit of knowledge, let's pause and look a little at how Python works with different types of objects.

BTW, have you ever modified a variable without knowing it or wanting to? I mean:

BTW, have you ever modified a variable without knowing it or wanting to? I mean:
```
>>> a = 1
>>> b = a
>>> a = 2
>>> b
1
>>>
```

Ok. But what about this?
```
>>> l = [1, 2, 3]
>>> m = l
>>> l[0] = 'x'
>>> m
['x', 2, 3]
>>>
```

This project is a little bit different than the usual projects. The first part is only questions about Python’s specificity like “What would be the result of…”. You should **read all documentation first (as usual :))**, then take the time to **think and brainstorm with your peers** about what you think and why. **Try to do this without coding anything for a few hours**

Trying examples in the Python interpreter will give you most of the answers without having to think about it. **Don’t go this route**. First read, then think, then brainstorm together. Only then you can test in the interpreter.

It’s important that you truly understand the reasons behind the answers of all those tasks so that you can apply the same logic to other variables and other variable types.

**You will most likely have to answer to these type of questions** during interviews for Python positions.

All answers should be only one line in a file. No space before or after the answer.


## Resources

**Read or watch:**

* [9.10. Objects and values](https://www.openbookproject.net/thinkcs/python/english2e/ch09.html#objects-and-values)
* [9.11. Aliasing](https://www.openbookproject.net/thinkcs/python/english2e/ch09.html#aliasing)
* [Immutable vs nutable types](https://stackoverflow.com/questions/8056130/immutable-vs-mutable-types)
* [Muttions](https://www.composingprograms.com/pages/24-mutable-data.html) (_Only this chapter_)
* [9.12. Cloning lists](https://www.openbookproject.net/thinkcs/python/english2e/ch09.html#cloning-lists)
* [Python tuples: immutable but potentially changing](http://radar.oreilly.com/2014/10/python-tuples-immutable-but-potentially-changing.html)

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

### `.txt` Answer Files

* Only one line
* No Shebang
* All files should end with a new line

## Mandatory Tasks

### 0. Who am I?

What function would you use to get the type of an object?

Write the name of the function in the file, without `()`.

**Files:** [`0-answer.txt`](./0-answer.txt)

### 1. Where are you?

How do you get the variable identifier (which is the memory address in the CPython implementation)?

Write the name of the function in the file, without `()`.

**Files:** [`1-answer.txt`](./1-answer.txt)

### 2. Right count

In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.
```
>>> a = 89
>>> b = 100
```

**Files:**  [`2-answer.txt`](./2-answer.txt)

### 3. Right count =

In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.
```
>>> a = 89
>>> b = 89
```

**Files:** [`3-answer.txt`](./3-answer.txt)

### 4. Right count =

In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.
```
>>> a = 89
>>> b = a
```

**Files:** [`4-answer.txt`](./4-answer.txt)

### 5. Right count =+

In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.
```
>>> a = 89
>>> b = a + 1
```

**Files:** [`5-answer.txt`](./5-answer.txt)

### 6. Is equal

What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
```

**Files:** [`6-answer.txt`](./6-answer.txt)

### 7. Is the same


What do these 3 lines print?
```
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
```

**Files:** [`7-answer.txt`](./7-answer.txt)

### 8. Is really equal

What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)
```

**Files:** [`8-answer.txt`](./8-answer.txt)

### 9. Is really the same

What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)
```

**Files:** [`9-answer.txt`](./9-answer.txt)

### 10. And with a list, is it equal

What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3]
>>> print(l1 == l2)
```

**Files:** [`10-answer.txt`](./10-answer.txt)

### 11. And with a list, is it the same

What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3]
>>> print(l1 is l2)
```

**Files:** [`11-answer.txt`](./11-answer.txt)

### 12. And with a list, is it really equal

What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
```

**Files:** [`12-answer.txt`](./12-answer.txt)

### 13. And with a list, is it really the same

What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
```

**Files:** [`13-answer.txt`](./13-answer.txt)

### 14. List append

What does this script print?
```
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
```

**Files:** [`14-answer.txt`](./14-answer.txt)

### 15. List add

What does this script print?
```
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
```

**Files:** [`15-answer.txt`](./15-answer.txt)

### 16. Integer incrementation

What does this script print?
```
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```

**Files:** [`16-answer.txt`](./16-answer.txt)

### 17. List incrementation

What does this script print?
```
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
```

**Files:** [`17-answer.txt`](./17-answer.txt)

### 18. List assignation

What does this script print?
```
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```

**Files:** [`18-answer.txt`](./18answer.txt)

### 19. Copy a list object

Write a function `def copy_list(l):` that returns a **copy** of a list.
* The input list can contain any type of objects
* File should be maximum 3-line long (no documentation needed)
* Not allowed to import any module
```
user@ubuntu:~/0x09$ cat 19-main.py
#!/usr/bin/python3
copy_list = __import__('19-copy_list').copy_list

my_list = [1, 2, 3]
print(my_list)

new_list = copy_list(my_list)

print(my_list)
print(new_list)

print(new_list == my_list)
print(new_list is my_list)

user@ubuntu:~/0x09$ ./19-main.py
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
True
False
user@ubuntu:~/0x09$ wc -l 19-copy_list.py 
3 19-copy_list.py
user@ubuntu:~/0x09$ 
```

**Files:** [`19-copy_list.py`](./19-copy_list.py) , [`19.main.py`](./mainFiles/19-main.py)

### 20. Tuple or not?

```
a = ()
```
Is `a` a tuple? Answer with `Yes` or `No`.

**Files:** [`20-answer.txt`](./20-answer.txt)

### 21. Tuple or not?

```
a = (1, 2)
```
Is `a` a tuple? Answer with `Yes` or `No`.

**Files:** [`21-answer.txt`](./21-answer.txt)

### 22. Tuple or not?

```
a = (1)
```
Is `a` a tuple? Answer with `Yes` or `No`.

**Files:** [`22-answer.txt`](./22-answer.txt)

### 23. Tuple or not?

```
a = (1, )
```
Is `a` a tuple? Answer with `Yes` or `No`.

**Files:** [`23-answer.txt`](./23-answer.txt)

### 24. Who I am?

What does this script print?

```
a = (1)
b = (1)
a is b
```

**Files:** [`24-answer.txt`](./24-answer.txt)

### 25. Tuple or not

What does this script print?

```
a = (1, 2)
b = (1, 2)
a is b
```

**Files:** [`25-answer.txt`](./25-answer.txt)

### 26. Empty is not empty

What does this script print?

```
a = ()
b = ()
a is b
```

**Files:** [`26-answer.txt`](./26-answer.txt)

### 27. Still the same?

```
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
```
Will the last line of this script print `139926795932424`? Answer with `Yes` or `No`.

**Files:** [`27-answer.txt`](./27-answer.txt)

### 28. Smae or not?



**Files:** [`20-answer.txt`](./20-answer.txt)

## Optional Tasks

### 29. #pythonic



**Files:** [`100-magic_string.py`](./100-magic_string.py) , [`100.main.py`](./mainFiles/100-main.py)

### 30. Low memory cost


```

```

**Files:** [`101-locked_class.py`](./101-locked_class.py) , [`101.main.py`](./mainFiles/101-main.py)

### 31. int 1/3


```

```

**Files:** [`103-line1.txt`](./103-line1.txt) , [`103-line2.txt`](./103-line2.txt), [`103-init.py`](./mainFiles/103-init.py)

### 32. int 2/3


```

```

**Files:** [`104-line1.txt`](./104-line1.txt) , [`104-line2.txt`](./104-line2.txt), [`104-line3.txt`](./104-line3.txt) , [`104-line4.txt`](./104-line4.txt), [`104-line5.txt`](./104-line5.txt), [`104-init.py`](./mainFiles/104-init.py)

### 33. int 3/3


```

```

**Files:** [`105-line1.txt`](./105-line1.txt), [`105-init.py`](./mainFiles/105-init.py)

### 34. Clear strings


```

```

**Files:** [`106-line1.txt`](./106-line1.txt) , [`106-line2.txt`](./106-line2.txt), [`106-line3.txt`](./106-line3.txt) , [`106-line4.txt`](./106-line4.txt), [`106-line5.txt`](./106-line5.txt), [`106-string.py`](./mainFiles/104-string.py)
