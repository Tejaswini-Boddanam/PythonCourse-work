'''
def func(argv):
    if base_con:
        return
    func(updating argv)

func(para)

def productofn(n):
    if n==1:
        return 1
    return n*productofn(n-1)

print(productofn(5))

def display(ind):
    if ind == len(s):
        return
    display(ind+1)
    print(s[ind],end='')

s = 'Python Programming'
display(0)

def display(n):
    if n > len(s):
        return 
    print(s[:n])
    display(n+1)

s = 'python'
display(1)

def display(ind,w):
    if ind > len(s)-w:
        return
    print(s[ind:ind+w])
    display(ind+1,w)

s= 'python programming'
display(0,10)


def display(n):
    if n==0:
        return 0  
    return n%10+display(n//10)

n = 987654
print(display(n))

0 1 1 2 3 5 8 13 21 34...


'''
a = 0
b = 1 

n =10
for i in range(n-1):
    a,b = b,a+b
    print(b)































