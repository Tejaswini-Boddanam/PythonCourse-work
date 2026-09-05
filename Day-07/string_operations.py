Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
c= 'strings.py'
c.startswith('str')
True
c.startswith('python')
False
c.endswith('python')
False
c.endswith('py')
True
c.islower()
True
c.isupper()
False
>>> 'PYTHONV13'.isupper()
True
>>> c.isalpha()
False
>>> c.isalnum()
False
>>> '             '.isspace()
True
>>> 'h          '.isspace()
False
>>> 'this is a title'.istitle()
False
>>> 'This Is Title'.istitle()
True
>>> 'my@var'.isidentifier()
False
>>> 'my_var'.isidentifier()
True
>>> l=[]
>>> l=list()
>>> l=[1,12.3,2+3j,'str',[1,2,3],(1,2,3),{1,2,3},{1:1,2:2,3:3},None,True]
>>> l
[1, 12.3, (2+3j), 'str', [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2, 3: 3}, None, True]
>>> l=[1,1,1,1,1,]
>>> l
[1, 1, 1, 1, 1]
>>> type(l)
<class 'list'>
>>> l=[1,2,3,4]
>>> m=[5,6,7]
>>> l+m
[1, 2, 3, 4, 5, 6, 7]
>>> m*3
[5, 6, 7, 5, 6, 7, 5, 6, 7]
>>> l
[1, 2, 3, 4]
>>> l[3]
4
>>> l[-1]
4
>>> l[1:]
[2, 3, 4]
>>> l[:2]
[1, 2]
>>> l[::-1]
[4, 3, 2, 1]
