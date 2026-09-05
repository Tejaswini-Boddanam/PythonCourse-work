Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
c = 'python programming'
len(c)
18
ord('p')
112
ord('p')
112
ord(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    ord(a)
NameError: name 'a' is not defined
ord('a')
97
ord
<built-in function ord>




ord('o')
111
ord('A')
65
chr(65)
'A'
chr(66)
'B'
chr(95)
'_'
chr(44)
','
min(c)
' '
max(c)
'y'
sorted(c)
[' ', 'a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 'r', 't', 'y']
c= 'string is immutable'
c
'string is immutable'
c.upper()
'STRING IS IMMUTABLE'
c.lower()
'string is immutable'
c.capitalize()
'String is immutable'
c.title()
'String Is Immutable'
c.swapcase()
'STRING IS IMMUTABLE'
'STEARSHYGHJDUEDBKCaf'.casefold()
'stearshyghjduedbkcaf'
'c'
'c'
c
'string is immutable'
c.center(60,'0')
'00000000000000000000string is immutable000000000000000000000'
c.ljust(60,'-')
'string is immutable-----------------------------------------'
c.rjust(60,'-')
'-----------------------------------------string is immutable'
'12'.zfill(4)
'0012'
'24'.zfill(5)
'00024'
'123456'.zfill(6)
'123456'
c
'string is immutable'
c.find('i')
3
c.find('z')
-1
c.rfind('i')
10
c
'string is immutable'
c.index('i')
3
c.rindex('i)
         
SyntaxError: unterminated string literal (detected at line 1)
c.rindex('i')
         
10
c.index('z')
         
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    c.index('z')
ValueError: substring not found
c.count('g')
         
1
c.count('m')
         
2
c.count('i')
         
3
c
         
'string is immutable'
c.replace('i','0')
         
'str0ng 0s 0mmutable'
c.replace('string','Float')
         
'Float is immutable'
c.maketrans('aeiou','12345')
         
{97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
c.translate(c.maketrans('aeiou','12345'))
         
'str3ng 3s 3mm5t1bl2'
c.replace('i','0')
         
'str0ng 0s 0mmutable'
c
         
'string is immutable'
c.split()
         
['string', 'is', 'immutable']
'string,is,immutable'
         
'string,is,immutable'
'string,is,immutable'.split()
         
['string,is,immutable']
'string,is,immutable'.split(',')
         
['string', 'is', 'immutable']
KeyboardInterrupt
'string,is,immutable'.rsplit(',')
         
['string', 'is', 'immutable']
'string,is,immutable'.rsplit('-')
         
['string,is,immutable']
'string,is,immutable'.rsplit('_')
         
['string,is,immutable']
s='''
python
programming
lang'''
         
s
         
'\npython\nprogramming\nlang'
s.splitlines()
         
['', 'python', 'programming', 'lang']
['', 'python', 'programming', 'lang'].join()
         
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    ['', 'python', 'programming', 'lang'].join()
AttributeError: 'list' object has no attribute 'join'
''.join(['','python','programming','lang',])
         
'pythonprogramminglang'
>>> ' '.join(['','python','programming','lang',])
...          
' python programming lang'
>>> '-
...          '.join(['','python','programming','lang',])
...          
SyntaxError: unterminated string literal (detected at line 1)
>>> '_'.join(['','python','programming','lang',])
...          
'_python_programming_lang'
>>> s.partition(',')
...          
('\npython\nprogramming\nlang', '', '')
>>> s='java,python,c,c++'
...          
>>> s.partition(',')
...          
('java', ',', 'python,c,c++')
>>> s.rpartition(',')
...          
('java,python,c', ',', 'c++')
>>> c= 'hello           world'          '
...          
SyntaxError: unterminated string literal (detected at line 1)
>>> c = '        Hello         world      '
...          
>>> c
...          
'        Hello         world      '
>>> c.strip()
...          
'Hello         world'
>>> c.lstrip()
...          
'Hello         world      '
>>> c.rstrip()
...          
'        Hello         world'
>>> text = "Hello world"
...          
>>> text.encode()
...          
b'Hello world'
>>> b'Hello world'.decode()
...          
'Hello world'
