Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s1 = 'hello'
type(s1)
<class 'str'>
id(s1)
2164863153664
s2 = 'hi'
id(s2)
140719968171448
s3 = s1
id(s3)
2164863153664
s3
'hello'
s1
'hello'
s1 = 'hi'
id(s1)
140719968171448
s1 = 'india'
id(s1)
2164865833632


list1 = [10,20,30,40]
list1
[10, 20, 30, 40]
list1
[10, 20, 30, 40]
type(list1)
<class 'list'>
list1[0]
10
list[1]
list[1]
list1[1]
20
list1[2]
30
list1[3]
40
list1[4]
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    list1[4]
IndexError: list index out of range
list1[-1]
40
list1[0:3]
[10, 20, 30]
list1[0:3:2]
[10, 30]
list2 = list('hi', 'hello')
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    list2 = list('hi', 'hello')
TypeError: list expected at most 1 argument, got 2
s1
'india'
list2 = list(s1)
list2
['i', 'n', 'd', 'i', 'a']
list3 = list1
list3
[10, 20, 30, 40]
id(list1)
2164820471616
id(list3)
2164820471616
list4 = ['hii', 100, True, 100, 67.90]
list4
['hii', 100, True, 100, 67.9]
list4[3] = 23
list4
['hii', 100, True, 23, 67.9]
list4[5] = 30
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    list4[5] = 30
IndexError: list assignment index out of range
list4.append('hey')
list4
['hii', 100, True, 23, 67.9, 'hey']
list4.remove('hey')
list4
['hii', 100, True, 23, 67.9]
list4.append(2000)
list4
['hii', 100, True, 23, 67.9, 2000]
list4.remove(5)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    list4.remove(5)
ValueError: list.remove(x): x not in list
list4.count(23)
1
list1
[10, 20, 30, 40]
id(list1)
2164820471616
list1.insert(2,200)
list1
[10, 20, 200, 30, 40]
id(list1)
2164820471616
list1.pop()
40
list1.pop(2)
200
list1
[10, 20, 30]
list2
['i', 'n', 'd', 'i', 'a']
list2.clear()
list2
[]
del(list2)
list2
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    list2
NameError: name 'list2' is not defined. Did you mean: 'list1'?
list2 = list1
list1
[10, 20, 30]
list2
[10, 20, 30]
id(list1)
2164820471616
id(list2)
2164820471616
list1[1] = 200
list1
[10, 200, 30]
list2
[10, 200, 30]
list2 = list(list1)
list1
[10, 200, 30]
list2
[10, 200, 30]
id(list1)
2164820471616
id(list2)
2164865872000
list1[1] = 20
list1
[10, 20, 30]
list2
[10, 200, 30]


tuple1 = (11,22,33,44,55)
tuple1
(11, 22, 33, 44, 55)
tuple[1]
tuple[1]
tuple1[1]
22
tuple1[30]
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    tuple1[30]
IndexError: tuple index out of range
tuple1[3] = 333
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    tuple1[3] = 333
TypeError: 'tuple' object does not support item assignment
tuple1[0:4:2]
(11, 33)
tuple1.index(44)
3
tuple1.count(22)
1
tuple2 = tuple1
tuple2
(11, 22, 33, 44, 55)
tuple3 = tuple(list1)
tuple3
(10, 20, 30)
list1
[10, 20, 30]
list1.append(tuple1)
list1
[10, 20, 30, (11, 22, 33, 44, 55)]
list1[0]
10
list1[1]
20
list1[2]
30
list1[3]
(11, 22, 33, 44, 55)
list1[3][2]
33
list5 = list(tuple1)
list5
[11, 22, 33, 44, 55]



set1 = {10,20,30,40}
set1
{40, 10, 20, 30}
sset1[2]
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    sset1[2]
NameError: name 'sset1' is not defined. Did you mean: 'set1'?
set1.add(50)
set1
{40, 10, 50, 20, 30}
set1.add(25)
set1
{40, 10, 50, 20, 25, 30}
set1.add('25')
set1
{40, 10, '25', 50, 20, 25, 30}
set1.add(25)
>>> set1
{40, 10, '25', 50, 20, 25, 30}
>>> set2 = set(set1)
>>> set2
{50, 20, 40, 25, 10, '25', 30}
>>> set2.remove('25')
>>> set2
{50, 20, 40, 25, 10, 30}
>>> se1
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    se1
NameError: name 'se1' is not defined. Did you mean: 's1'?
>>> set1
{40, 10, '25', 50, 20, 25, 30}
>>> set1.union(set2)
{40, 10, '25', 50, 20, 25, 30}
>>> set1.intersection(set2)
{40, 10, 50, 20, 25, 30}
>>> set1.add(list1)
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    set1.add(list1)
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
>>> set1.add(tuple1)
>>> set1
{40, 10, (11, 22, 33, 44, 55), '25', 50, 20, 25, 30}
