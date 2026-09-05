'''
res = {i for i in range(1,11)}
print(res)

n = 12
res = {i for i in range(1,n+1) if n%i==0}
print(res)

r = [12,23,45,687,34,123,34,12,43,90]
res = {i if i%2==0 else 0 for i in r}
print(res)

r = [[12,23,45],[687,34,123],[34,43,90]]
res = {j for i in r for j in i if j%2==0}
print(res)
'''
'''
l=[int(input(f"Enter the number - {i+1}: "))for i in range(10)]
print(l)
'''

'''
names = [input(f"Enter the name - {i+1}") for i in range(5)]
print(names)
'''

'''
names = {input(f"Enter the name-{i+1}: "):int(input("Enter the marks: "))for i in range(5)}
print(names)
'''

'''
res = {i:i*i for i in range(1,11)}
print(res)
'''

'''
res = [(x, y)for x in range(3) for y in range(3)if x!=y]
print(res)
'''

'''
numbers = [1,2,3,4,5]
result = [x * x for x in numbers]
print(result)
'''
'''result = [x for x in range(1,11)if x % 2==0]
print(result)
'''

