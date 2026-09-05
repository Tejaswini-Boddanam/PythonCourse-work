Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> l= [1,2,3,4,5]
>>> l= [10,9,6,1,2,3,4]
>>> l
[10, 9, 6, 1, 2, 3, 4]
>>> id(l)
2305036105152
>>> l.append(12)
>>> l
[10, 9, 6, 1, 2, 3, 4, 12]
>>> l.append(14)
>>> l
[10, 9, 6, 1, 2, 3, 4, 12, 14]
>>> id(l)
2305036105152
>>> l.insert(1,13)
>>> l
[10, 13, 9, 6, 1, 2, 3, 4, 12, 14]
>>> l.extend([52,32,42])
>>> l
[10, 13, 9, 6, 1, 2, 3, 4, 12, 14, 52, 32, 42]
>>> id(l)
2305036105152
>>> l[3]
6
>>> l.pop()
42
>>> l.pop(3)
6
>>> l.remove(4)
>>> l
[10, 13, 9, 1, 2, 3, 12, 14, 52, 32]
>>> del l[1]
>>> l
[10, 9, 1, 2, 3, 12, 14, 52, 32]
>>> l.clear()
>>> l
[]
>>> id(l)
2305036105152
>>> l=[10, 13, 9, 6, 1, 2, 3, 4, 12, 14]
>>> l
[10, 13, 9, 6, 1, 2, 3, 4, 12, 14]
>>> max(1)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    max(1)
TypeError: 'int' object is not iterable
max(l)
14
min(1)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    min(1)
TypeError: 'int' object is not iterable
min(l)
1
sorted(l)
[1, 2, 3, 4, 6, 9, 10, 12, 13, 14]
l
[10, 13, 9, 6, 1, 2, 3, 4, 12, 14]
l.reverse()
l
[14, 12, 4, 3, 2, 1, 6, 9, 13, 10]
l.sort()
l
[1, 2, 3, 4, 6, 9, 10, 12, 13, 14]
l.sort(reverse=True)
l
[14, 13, 12, 10, 9, 6, 4, 3, 2, 1]
sum(l)
74
l = [1,2,3]
m = [1,2,3]
l
[1, 2, 3]
n = l
n.append(4)
n
[1, 2, 3, 4]
l
[1, 2, 3, 4]
m = l.copy()
m
[1, 2, 3, 4]
m.append(10)
m
[1, 2, 3, 4, 10]
l
[1, 2, 3, 4]
all([0,'',[],(),set(),{},False])
False
all([1,'',[],(),{},False])
False
any([1,'',[],(),set(),{},False])
True
l
[1, 2, 3, 4]
l.index(3)
2
l.index(5)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    l.index(5)
ValueError: list.index(x): x not in list
l
[1, 2, 3, 4]
l.count(3)
1
l.count(5)
0
l
[1, 2, 3, 4]
l=[[1,2,3,4],[5,6,7,8]]
l
[[1, 2, 3, 4], [5, 6, 7, 8]]
l[0]
[1, 2, 3, 4]
l[1]
[5, 6, 7, 8]
l[0][2]
3
l[1][3]
8
l[-1][-1]
8
t=()
t=tuple()
t=(1,12.3,3+5j,"str",[1,2,3],(1,2,3){1,2},{1:1},True)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
