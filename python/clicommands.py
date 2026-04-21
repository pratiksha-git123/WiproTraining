Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a = 5
b = a
a is b
True
a = 5
b = float(a)
b
5.0
a= 525
b = float(a)
b
525.0
a = 40
b = 40
type(a)
<class 'int'>
type(b)
<class 'int'>
c = a+b
c
80
type(c)
<class 'int'>
a = 5
 b = str(a)
 
SyntaxError: unexpected indent
<class 'int'>b = str(a)
KeyboardInterrupt
<class 'int'>b = str(a)
SyntaxError: invalid syntax




b = str(a)
b
'5'
e = int(b)
e
5
x = 'hi'
y = int(x)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    y = int(x)
ValueError: invalid literal for int() with base 10: 'hi'
y = bool(x)
y
True
x = 'i'
y = x
y = int(y)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    y = int(y)
ValueError: invalid literal for int() with base 10: 'i'
x = 'i'
y = ord(x)
y
105
x = "
SyntaxError: unterminated string literal (detected at line 1)
x = ''
y = bool(x)
y
False
x = 'hiiiiiiii'
y = bool(x)
y
True
print('hii')
hii
print(6)
6
print(6+3)
9
print('ans', 6+3)
ans 9
>>> print('ans:' , '6+3')
ans: 6+3
>>> print("my brother's house")
my brother's house
>>> print('my brother's house)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> input()
67
'67'
>>> p = input
>>> p = input()
hii
>>> p
'hii'
>>> p = input('type something:')
type something:6745
>>> p
'6745'
>>> p = int(input('type something:'))
type something:7890
>>> p
7890
