
'''
def display(name,email,password):
    print(f'Hello {name},')
    print(f'Your email:{email}')
    print(f'Your password:{password}')

display('Teju','Teju@gmail.com','Teju123@')
display('Dhana','Dhana@gmail.com','dhana123@')
display('sathwika','sathwika@gmsil.com','sathwika123@')
display('pavani','pavani@gmail.com','pavani@123
'''

'''
def isleapyear(year):
    if year%400 ==0 or (year%4==0 and year%100!=0):
        print(f"{year} is leap year")
    else:
        print(f"{year} is not leap year")

for year in range(2001,2027):
    isleapyear(year)
    '''

    

'''
def sumofdigits(n):
    sum = 0
    while n>0:
        sum += n%10
        n=n//10
    return sum

n = int(input("Enter the number:"))
print(f'sum of{n} digits is {sumofdigits(n)}')
'''

'''
def productofdigits(n):
    pro = 1
    while n>0:
        pro *= n%10
        n=n//10
    return pro

n = int(input("Enter the number:"))
print(f'product of {n} digits is {productofdigits(n)}')
'''


'''
def checkpassword(password):
    if len(password) > 8:
        check = set()
        for i in password:
            if i.isupper():
                check.add('u')
            elif i.islower():
                check.add('l')
            elif i.isdigit():
                check.add('d')
            else:
                check.add('s')
        if len(check) == 4:
            return "strong password"
    return "Weak password"

password = input("Enter the password")
print(f'password is {checkpassword(password)}')
'''

'''
def table(n):
    print(f'------------Table - {n}--------------------')
    for i in range(1,11):
        print(f'{n} * {i} = {n*i}')

for i in range(1,21):
    table(i)
    '''

n = int(input('Enter the units'))
if 0



