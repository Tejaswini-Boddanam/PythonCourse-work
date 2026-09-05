Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=20
b=10
a+b
30
a-b
10
a*b
200
a/b
2.0
9/2
4.5
a//b
2
9//2
4
9%2
1
2**3
8
4**2
16
a
20
b
10
a<b
False
a>b
True
a<=b
False
a>=b
True
a==b
False
a!=b
True
c=10
c
10
c +=10
c
20
c -=10
c
10
c *=2
c
20
c //=2
c
10
c **=2
c
100
c %=3
c
1
c /=2
c
0.5
n = 10
n
10
n%2==0 and n%3==0
False
n%2==0 or  n%3==0
True
n%8==0 or n%3==0
False
n
10
n<5
False
not n<5
True
#str list tuple set dict
s='codegnan'
'e' in s
True
'z' in s
False
'f' not in s
True
'o' not in s
False
l=[1,2,3,4]
4 in l
True
2 in l
True
6 not in l
True
8 in l
False
t=(1,2,3,4)
1 in t
True
5 not in t
True
s={1,2,3,4,5,6,7}
6 in s
True
8 not in s
True
d={'name':'abdul','batch':63,'course':'python'}
'name' in d
True
'abdul' in d
False
63 in d
False
'python' in d
False
l=[1,2,3,4]
m=[1,2,3,4]
id(l)
2621152134592
id(m)
2621107784640
l is m
False
n = l
id(n)
2621152134592
l is n
True
l is not m
True
l is not n
False
a
20
id(a)
140711416547032
s={1,2,3,4}
id(s)
2621151846784
s.add(5)
s
{1, 2, 3, 4, 5}
id(s)
2621151846784
9&10
8
9|10
11
9^10
3
8>>2
2
8<<2
32

8>>3
1
~8
-9
>>> ~12
-13
>>> ~45
-46
>>> a=10
>>> b=10.3
>>> c='codegnan'
>>> print(a,b,c)
10 10.3 codegnan
>>> print("a value is",a)
a value is 10
>>> print("a value is",a,"| b value is",b,'|c value is',c)
a value is 10 | b value is 10.3 |c value is codegnan
>>> print(a,b,c)
10 10.3 codegnan
>>> print("a value is",a)
a value is 10
>>> print("a value is",a,"|b value is",b,'| c value is',c)
a value is 10 |b value is 10.3 | c value is codegnan
>>> print(a,b,c)
10 10.3 codegnan
>>> print("a value is",a)
a value is 10
>>> print("a value is",a,"| b value is",b,'| c value is',c)
a value is 10 | b value is 10.3 | c value is codegnan
>>> print(a,b,c)
10 10.3 codegnan
>>> print(a,b,c,sep='')
1010.3codegnan
>>> print(a,b,c,sep='\n')
10
10.3
codegnan
>>> print(a,b,c,sep='\n')
10
10.3
codegnan
>>> print(a,b,c,sep='\t')
10	10.3	codegnan
>>> print(a,b,c,sep='/t',end='@')
10/t10.3/tcodegnan@
>>> print(f'a={a} b={b} c={c}')
a=10 b=10.3 c=codegnan
>>> print(f"a value is {a} |b value is {b} |c value is {c}")
a value is 10 |b value is 10.3 |c value is codegnan
