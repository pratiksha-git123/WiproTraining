Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s1 = 'hello'
s1
'hello'
type(s1)
<class 'str'>
s1.capitalize
<built-in method capitalize of str object at 0x000001EF766935D0>
s1.capitalize()
'Hello'
s1.upper()
'HELLO'
s1.lower()
'hello'
s1 = "hEllO"
s1.casefold()
'hello'
s1 = "HeLLo"
s1.casefold()
'hello'
s1.count(l)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s1.count(l)
NameError: name 'l' is not defined
s1.count("l")
0
s1 = "HELLO"
s1.count("H")
1
s1.endswith("O")
True
s1.find("L")
2
s1.index("O")
4
s1.isalpha()
True
s1.isdigit()
False
s1.replace("L","*")
'HE**O'

====================================================== RESTART: C:/WiproTraining/python/str1ex.py ======================================================
h
e
l
l
o
 
w
o
r
l
d
!
!
!
>>> 
====================================================== RESTART: C:/WiproTraining/python/str1ex.py ======================================================
h
e
l
l
o
>>> 
====================================================== RESTART: C:/WiproTraining/python/str1ex.py ======================================================
h
e
l
l
o
