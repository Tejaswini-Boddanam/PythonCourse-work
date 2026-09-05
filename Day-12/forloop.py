#range(start,end+1,step) => (0,nodef,1)
for i in range(1,11):
    print(i)

for i in range(2,51,2):
    print(i,end=' ')

for i in range(1,100,2):
    print(i,end=' ')

for i in range(5,51,5):
    print(i)

n = int(input("Enter the table no: "))
for i in range(1,11):
    print(f'{n} = {i} = {n*i}')