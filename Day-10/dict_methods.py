Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
data = {'name': 'sajid','batch':63,'course':'PFS'}
data['name']
'sajid'
data['batch']
63
data['course']
'PFS'
63 in data
False
data['age']
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    data['age']
KeyError: 'age'
data.get('age',key is not present')
         
SyntaxError: unterminated string literal (detected at line 1)
data.get('age','key is not present')
         
'key is not present'
data.get('course','key is not present')
         
'PFS'
data['batch']=64
         
data
         
{'name': 'sajid', 'batch': 64, 'course': 'PFS'}
data['skills'] = ['python','mysql','flask']
         
data
         
{'name': 'sajid', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask']}
data['age']=21
         
data
         
{'name': 'sajid', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'age': 21}
data.update({'phno':9515626942,'email':'tejaswinib@gmail.com'})
         
data
         
{'name': 'sajid', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'age': 21, 'phno': 9515626942, 'email': 'tejaswinib@gmail.com'}
data.pop('age')
         
21
data
         
{'name': 'sajid', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'phno': 9515626942, 'email': 'tejaswinib@gmail.com'}
data.pop('phnnumber')
         
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    data.pop('phnnumber')
KeyError: 'phnnumber'
data.pop('phno')
         
9515626942
data
         
{'name': 'sajid', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'email': 'tejaswinib@gmail.com'}
del data['name']
         
data
         
{'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'email': 'tejaswinib@gmail.com'}
data.popitem()
         
('email', 'tejaswinib@gmail.com')
data
         
{'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask']}
data.popitem()
         
('skills', ['python', 'mysql', 'flask'])
data
         
{'batch': 64, 'course': 'PFS'}
data.clear()
         
data
         
{}
data = {'name': 'sajid', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'age': 21, 'phno': 9515626942, 'email': 'tejaswinib@gmail.com'}
         
data
         
{'name': 'sajid', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'age': 21, 'phno': 9515626942, 'email': 'tejaswinib@gmail.com'}
data.keys()
         
dict_keys(['name', 'batch', 'course', 'skills', 'age', 'phno', 'email'])
data.values()
         
dict_values(['sajid', 64, 'PFS', ['python', 'mysql', 'flask'], 21, 9515626942, 'tejaswinib@gmail.com'])
data.items()
         
dict_items([('name', 'sajid'), ('batch', 64), ('course', 'PFS'), ('skills', ['python', 'mysql', 'flask']), ('age', 21), ('phno', 9515626942), ('email', 'tejaswinib@gmail.com')])
sorted(data)
         
['age', 'batch', 'course', 'email', 'name', 'phno', 'skills']
sorted(data,reverse=True)
         
['skills', 'phno', 'name', 'email', 'course', 'batch', 'age']
max(data)
         
'skills'
min(data)
         
'age'
data
         
{'name': 'sajid', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'age': 21, 'phno': 9515626942, 'email': 'tejaswinib@gmail.com'}
data['age']
         
21
data.get('age')
         
21
data.setdefault('age',0)
         
21
data
         
{'name': 'sajid', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'age': 21, 'phno': 9515626942, 'email': 'tejaswinib@gmail.com'}
data.get('age')
         
21
data.setdefault('name','')
         
'sajid'
data
         
{'name': 'sajid', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'age': 21, 'phno': 9515626942, 'email': 'tejaswinib@gmail.com'}
len(data)
         
7
>>> all(data)
...          
True
>>> any(data)
...          
True
>>> data
...          
{'name': 'sajid', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'age': 21, 'phno': 9515626942, 'email': 'tejaswinib@gmail.com'}
>>> a={1:1,2:2}
...          
>>> b=a
...          
>>> a
...          
{1: 1, 2: 2}
>>> b
...          
{1: 1, 2: 2}
>>> c= a.copy()
...          
>>> c[4]=4
...          
>>> c
...          
{1: 1, 2: 2, 4: 4}
>>> a
...          
{1: 1, 2: 2}
>>> d = dict.fromkeys(["a","b"],0)
...          
>>> d
...          
{'a': 0, 'b': 0}
>>> 
>>> 

... 
... 
>>> 

>>> 

... 
... 
>>> 












































































































































































































































































































































































