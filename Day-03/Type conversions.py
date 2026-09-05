Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=10
>>> a
10
>>> float(a)
10.0
>>> complex(a)
(10+0j)
>>> str(a)
'10'
>>> list(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
>>> tuple(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
>>> set(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
>>> bool(a)
True
>>> b=1.0
>>> int(b)
1
>>> complex(b)
(1+0j)
>>> str(b)
'1.0'
>>> list(b)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
>>> tuple(b)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
dict(b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
bool(b)
True
com=1+2j
int(com)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    int(com)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(com)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    float(com)
TypeError: float() argument must be a string or a real number, not 'complex'
str(com)
'(1+2j)'
list(com)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    list(com)
TypeError: 'complex' object is not iterable
tuple(com)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    tuple(com)
TypeError: 'complex' object is not iterable
set(com)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    set(com)
TypeError: 'complex' object is not iterable
dict(com)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    dict(com)
TypeError: 'complex' object is not iterable
c="reena"
int(c)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    int(c)
ValueError: invalid literal for int() with base 10: 'reena'
float(c)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    float(c)
ValueError: could not convert string to float: 'reena'
complex(c)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    complex(c)
ValueError: complex() arg is a malformed string
list(c)
['r', 'e', 'e', 'n', 'a']
tuple(c)
('r', 'e', 'e', 'n', 'a')
set(c)
{'n', 'e', 'r', 'a'}
dict(c)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    dict(c)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
bool(c)
True
l=[1,2,3,4,5,'sra',4,5]
int(l)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(l)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
complex(l)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    complex(l)
TypeError: complex() argument must be a string or a number, not list
str(l)
"[1, 2, 3, 4, 5, 'sra', 4, 5]"
tuple(l)
(1, 2, 3, 4, 5, 'sra', 4, 5)
set(l)
{1, 2, 3, 4, 5, 'sra'}
dict(l)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    dict(l)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
bool(l)
True
t=(1,2,3,4,5)
int(t)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(t)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a real number, not 'tuple'
str(t)
'(1, 2, 3, 4, 5)'
list(t)
[1, 2, 3, 4, 5]
dict(t)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    dict(t)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
bool(t)
True
s1={1{1,2,3,4,5}
    
SyntaxError: '{' was never closed
s1={1,2,3,4,5}
    
a={1:'teju:,2:'lot'}"
   
SyntaxError: unterminated string literal (detected at line 1)
