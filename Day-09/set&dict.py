'''
s=set()
s={1,2,3,4,12,324,9876,34,12431324}
s
{1, 2, 3, 324, 4, 34, 12, 9876, 12431324}
s=set()
s.add(1)
s.add(12.3)
s.add(2+4j)
s.add("str")
s.add([1,2,3])
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    s.add([1,2,3])
TypeError: unhashable type: 'list'
s
{1, 'str', 12.3, (2+4j)}
s={1,1,1,1,1,1,1}
s
{1}
l={10,20,30}
m={1,2,3,4}
l+m
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    l+m
TypeError: unsupported operand type(s) for +: 'set' and 'set'
a=[1,2,3,4,5]
b=[3,5,7,9]
a
[1, 2, 3, 4, 5]
b
[3, 5, 7, 9]
a|b
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a|b
TypeError: unsupported operand type(s) for |: 'list' and 'list'
a={1,2,3,4,5}
b={3,5,7,9}
a|b
{1, 2, 3, 4, 5, 7, 9}
a&b
{3, 5}
a-b
{1, 2, 4}
a^b
{1, 2, 4, 7, 9}
#{1}{2}{3}{4}{5}{1,2},{2,3},{3,4},{1,4},{1,2,3,4}
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
  File "<pyshell#38>", line 1, in <module>
    a.superset(b)
AttributeError: 'set' object has no attribute 'superset'. Did you mean: 'issuperset'?
a.issuperset(b)
False
a
{1, 2, 3, 4, 5}
5 in a
True
7 in a
False
8 not in a
True
a
{1, 2, 3, 4, 5}
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
b.add(12)
b
{1, 2, 3, 4, 5, 12}
a
{1, 2, 3, 4, 5, 12}
c=a.copy()
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
a.remove(16)
a
{4, 5, 12, 17, 18, 123}
a.remove(12)
a
{4, 5, 17, 18, 123}
a.remove(12)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    a.remove(12)
KeyError: 12
a.discard(12)
a.discard(5)
a
{4, 17, 18, 123}
a.clear()
a
set()
a={1,2,3,4,5}
a.update({"str",0,12,13,-1,-23.4})
a
{0, 1, 2, 3, 4, 5, -23.4, 12, 13, 'str', -1}
len(a)
11
all(a)
False
any(a)
True
a=frozenset({1,12,13,10,18,59,20})
a
frozenset({1, 18, 20, 10, 59, 12, 13})
a.add(12)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    a.add(12)
AttributeError: 'frozenset' object has no attribute 'add'
d={}
d=dict()
type(d)
<class 'dict'>
d={'k1':'v1','k2':'v2','k3':'v3'}
d
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
id(d)
2813558563008
d['k4']='v4'
d
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}
id(d)
2813558563008
d['k1']='v11'
d
{'k1': 'v11', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}
d['k5']='v4'
d
{'k1': 'v11', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4', 'k5': 'v4'}
d={}
d[1]='int'
d
{1: 'int'}
d[12.3]='float'
d
{1: 'int', 12.3: 'float'}
d[2+3j]='complex'
d
{1: 'int', 12.3: 'float', (2+3j): 'complex'}
d['str']='string'
d
{1: 'int', 12.3: 'float', (2+3j): 'complex', 'str': 'string'}
d[(1,2,3,4)]='tuple'
d
{1: 'int', 12.3: 'float', (2+3j): 'complex', 'str': 'string', (1, 2, 3, 4): 'tuple'}
d={}
d[1]=1
d[2]=12.3
d[3]=12+4j
d[4]='str'
d[5]=[1,2,3,4]
d[6]=(1,2,3)
d[7]=[1,2,3]
d[8]={1:1}
>>> d[9]=True
>>> d
{1: 1, 2: 12.3, 3: (12+4j), 4: 'str', 5: [1, 2, 3, 4], 6: (1, 2, 3), 7: [1, 2, 3], 8: {1: 1}, 9: True}
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
>>> d[10]
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    d[10]
KeyError: 10
>>> d.get(10)
>>> d.get(1)
1
>>> d.get(10,"key is not present")
'key is not present'
>>> d.get(6,"key is not present")
(1, 2, 3)
>>> d[3]=4
>>> d
{1: 1, 2: 12.3, 3: 4, 4: 'str', 5: [1, 2, 3, 4], 6: (1, 2, 3), 7: [1, 2, 3], 8: {1: 1}, 9: True}
>>> d[5]=10
>>> d
{1: 1, 2: 12.3, 3: 4, 4: 'str', 5: 10, 6: (1, 2, 3), 7: [1, 2, 3], 8: {1: 1}, 9: True}
>>> d[6]=12
>>> d
{1: 1, 2: 12.3, 3: 4, 4: 'str', 5: 10, 6: 12, 7: [1, 2, 3], 8: {1: 1}, 9: True}
>>> d[7]=20
>>> d
{1: 1, 2: 12.3, 3: 4, 4: 'str', 5: 10, 6: 12, 7: 20, 8: {1: 1}, 9: True}
'''
