'''
def display(name,email,password):
    print(f'name: {name}')
    print(f'email: {email}')
    print(f'password: {password}')

display('xyz','xyz@gmail.com','xyz@123')
display('xyz@123','xyz@gmail.com','xyz')
display('xyz@gmail.com','xyz@123','xyz')
'''


'''
def display(name,email,password):
    print(f'name: {name}')
    print(f'email: {email}')
    print(f'password: {password}')
    
display(name='xyz',email='xyz@gmail.com',password='xyz@123')
display(password='xyz@123',email='xyz@gmail.com',name='xyz')
display(email='xyz@gmail.com',password='xyz@123',name='xyz')
'''

'''
def display(name,email='gmail.com',password=''):
    print(f'name: {name}')
    print(f'email: {email}')
    print(f'password: {password}')

display('xyz','xyz@gmail.com','xyz@123')
display('xyz','xyz@gmail.com')
display('xyz')
'''

'''
def display(*names):
    print(names)

display('teju')
display('teju','dhana')
display('teju','dhana','kavya')
display('teju','dhana','kavya','pavani')
'''

def display(**products):
    print(products)

display(bag=5000)
display(bag=5000,book=30)
display(bag=5000,book=30,bottle=300)