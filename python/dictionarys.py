Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
dict1 = {1:10, 2:20, 3:30}
dict1
{1: 10, 2: 20, 3: 30}
dict1[2]
20
dict2 = {'a':10, 'b':20, 'c':30}
dict2
{'a': 10, 'b': 20, 'c': 30}
dict2['c']
30
>>> stud = {'rno':101, 'name':'AAA', 'city':'BBB'}
>>> stud
{'rno': 101, 'name': 'AAA', 'city': 'BBB'}
>>> stud[name]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    stud[name]
NameError: name 'name' is not defined
>>> stud['name']
'AAA'
>>> stud['name'] = 'XXX'
>>> stud
{'rno': 101, 'name': 'XXX', 'city': 'BBB'}
>>> stud['fname'] = 'YYY'
>>> stud
{'rno': 101, 'name': 'XXX', 'city': 'BBB', 'fname': 'YYY'}
>>> stud.get('name')
'XXX'
>>> stud.keys()
dict_keys(['rno', 'name', 'city', 'fname'])
>>> stud.values()
dict_values([101, 'XXX', 'BBB', 'YYY'])
>>> stud.pop('fname')
'YYY'
>>> stud
{'rno': 101, 'name': 'XXX', 'city': 'BBB'}
