''''
n = int(input("Enter the size:"))

for i in range(n):
    for j in range(n):
        if j == 0 or j == n-1 or i == j:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
    '''
'''
n = int(input("Enter the size:"))

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()


'''
'''
n = int(input("Enter the size:"))
m = n // 2

for i in range(n):
    for j in range(n):
        if j == 0 or i == 0 or i == m or (j == n-1 and i < m):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

'''
'''
n = int(input("Enter the size:"))

for i in range(n):
    for j in range(n):
        if (i == 0 or i == n-1 or j == 0 or j == n-1) or (i == j and i > n//2):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

'''
'''
n = int(input("Enter the size:"))
m = n // 2

for i in range(n):
    for j in range(n):
        if j == 0 or i == 0 or i == m or (j == n-1 and i < m) or (i-j == m):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
    
'''
'''
n = int(input("Enter the size:"))
m = n // 2

for i in range(n):
    for j in range(n):
        if i == 0 or i == m or i == n-1 or (j == 0 and i < m) or (j == n-1 and i > m):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
  
'''
'''
n = int(input("Enter the size:"))

for i in range(n):
    for j in range(n):
        if i == 0 or j == n//2:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

''' 
'''
n = int(input("Enter the size:"))

for i in range(n):
    for j in range(n):
        if j == 0 or j == n-1 or i == n-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
    
'''
'''
n = int(input("Enter the size:"))

for i in range(n):
    for j in range(n):
        if j == 0 or j == n-1 or (i == j and i >= n//2) or (i+j == n-1 and i >= n//2):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
   
'''
'''
n = int(input("Enter the size:"))

for i in range(n):
    for j in range(n):
        if i == j or i+j == n-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()


'''
'''
n = int(input("Enter the size:"))
m = n // 2

for i in range(n):
    for j in range(n):
        if (i == j and i <= m) or (i+j == n-1 and i <= m) or (j == m and i >= m):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
    
'''

n = int(input("Enter the size:"))

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or i+j == n-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
    