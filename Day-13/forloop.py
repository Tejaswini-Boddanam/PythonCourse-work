'''
s = 'python programming'
for i in range(len(s)):
    if s[i] in 'aeiouAEIOU':
        print(i,s[i])
'''
'''
l=[23,45,12,34,50,24,35,68,75,34,10]
sum=0
for i in range(len(l)):
    if l[i]%2==0:
        sum=sum+i
        print(i,l[i])
print(sum)
'''

'''
n= int(input("Enter the number: "))
fact = 1
for i in range(1,n+1):
    fact *=i
print(f"Factorial of {n} is {fact}")
'''

'''
n = int(input("Enter the no of students:"))
max_marks = 0
for i in range(n):
    name = input("Enter the name: ")
    marks = int(input("Enter the marks: "))
    if marks > max_marks:
        max_marks = marks
    data[name] = marks

'''
print(data)
print("Maximum Marks:",max_marks)
'''

n = int(input("Enter the no of products: "))
total_bill = 0
products = {}
for i in range(n):
    product = input(f"product - {i}: ")
    price = float(input(f"price - {i}: "))
    quantity = int(input(f"Quantity - {i}: "))
    final_price = price*quantity
    total_bill += final_price
    products[product] = f'{price} * {quantity} = {final_price}'
print(products)
print("Total Bill:",total_bill)
'''

