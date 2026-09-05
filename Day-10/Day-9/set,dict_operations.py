Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s = {}
type(s)
<class 'dict'>
s = set()
s = {1,2,3,4,12,324,9876,34,12345612}
s
{1, 2, 3, 4, 34, 324, 12, 12345612, 9876}
s = set()
s
set()
s
set()
s.add(1)
s.add(12.3)
s.add(2+4j)
s.add()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s.add()
TypeError: set.add() takes exactly one argument (0 given)
s={1,1,1,1,1,1}
s
{1}
a = {1,2,3,4,5}
b = {3,5,7,9}
a
{1, 2, 3, 4, 5}
b
{9, 3, 5, 7}
a | b
{1, 2, 3, 4, 5, 7, 9}
a & b
{3, 5}
a - b
{1, 2, 4}
a ^ b
{1, 2, 4, 7, 9}
{1}<=a
True
{1,2,3,4}<=a
True
a
{1, 2, 3, 4, 5}
{1,2,3,4,5}<=a
True
a
{1, 2, 3, 4, 5}
b
{9, 3, 5, 7}
a.isdisjoint(b)
False
a.isdisjoint({9,10})
True
a.union(b)
{1, 2, 3, 4, 5, 7, 9}
a.intersection(b)
{3, 5}
a.issubset(b)
False
a.superset(b)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    a.superset(b)
AttributeError: 'set' object has no attribute 'superset'. Did you mean: 'issuperset'?
a.issuperset(b)
False
a
{1, 2, 3, 4, 5}
5 in a
True
8 in a
False
12 not in a
True
max(a)
5
min(a)
1
sorted(a)
[1, 2, 3, 4, 5]
sum(a)
15
a
{1, 2, 3, 4, 5}
b=a
b
{1, 2, 3, 4, 5}
a
{1, 2, 3, 4, 5}
b.add(12)
b
{1, 2, 3, 4, 5, 12}
a
{1, 2, 3, 4, 5, 12}
c = a.copy()
c.add(12)
c.add(13)
c
{1, 2, 3, 4, 5, 12, 13}
a
{1, 2, 3, 4, 5, 12}
a.add(123)
a
{1, 2, 3, 4, 5, 123, 12}
a.update({16,17,18})
a
{1, 2, 3, 4, 5, 12, 16, 17, 18, 123}
a.pop()
1
a.pop()
2
a
{3, 4, 5, 12, 16, 17, 18, 123}
a.pop()
3
a.remove()
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    a.remove()
TypeError: set.remove() takes exactly one argument (0 given)
a.remove(16)
a
{4, 5, 12, 17, 18, 123}
a.remove(12)
a
{4, 5, 17, 18, 123}
a.discard(12)
a.disacard(5)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    a.disacard(5)
AttributeError: 'set' object has no attribute 'disacard'. Did you mean: 'discard'?
a.discard(5)
a
{4, 17, 18, 123}
a.clear()
a
set()
a = frozenset({1,12,13,10,18,59,20})
a
frozenset({1, 18, 20, 10, 59, 12, 13})
d = {}
d=dict()
type(d)
<class 'dict'>
d = {'k1':'v1','k2':'v2','k3':'v3'}
d
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
id(d)
2981208464000
d['k4'] = 'v4'
d
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}
d['k5'] = 'v4'
d
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4', 'k5': 'v4'}
d ={}
d[1]='int'
d
{1: 'int'}
d[12.3]='float'
d
{1: 'int', 12.3: 'float'}
d[2+3j]='com'
d
{1: 'int', 12.3: 'float', (2+3j): 'com'}
d['str']='string'
d
{1: 'int', 12.3: 'float', (2+3j): 'com', 'str': 'string'}
d[(1,2,3,4)]='tuple'
d
{1: 'int', 12.3: 'float', (2+3j): 'com', 'str': 'string', (1, 2, 3, 4): 'tuple'}
>>> d[1,2,3,4]='list'
>>> d
{1: 'int', 12.3: 'float', (2+3j): 'com', 'str': 'string', (1, 2, 3, 4): 'list'}
>>> d({1,2,3,,4})='set'
SyntaxError: invalid syntax
>>> d({1,2,3,4})='set'
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
>>> d = {}
>>> d[1]=1
>>> d[2]=12.3
>>> d[3]=12+4j
>>> d[4]='str'
>>> d[5]=[1,2,3,4]
>>> d[6]=(1,2,3)
>>> d[7]={1,2,3}
>>> d[8]={1:1}
>>> d[9]=True
>>> d
{1: 1, 2: 12.3, 3: (12+4j), 4: 'str', 5: [1, 2, 3, 4], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> 9 in d
True
>>> 10 in d
False
>>> 'str' in d
False
>>> d[5]
[1, 2, 3, 4]
>>> d[8]
{1: 1}
>>> d.get(10)
>>> d.get(1)
1
>>> d.get(10,"key is not present")
'key is not present'
>>> d.get(6,"key is not present")
(1, 2, 3)
>>> d[5]=10
>>> d
{1: 1, 2: 12.3, 3: (12+4j), 4: 'str', 5: 10, 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> d[6]=12
>>> d
{1: 1, 2: 12.3, 3: (12+4j), 4: 'str', 5: 10, 6: 12, 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> d[7]=20
>>> d
{1: 1, 2: 12.3, 3: (12+4j), 4: 'str', 5: 10, 6: 12, 7: 20, 8: {1: 1}, 9: True}
