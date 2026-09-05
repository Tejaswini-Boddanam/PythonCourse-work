'''
i=1
while i<=10:
    print(i)
    i+=1
    '''
'''
i = 10
while i>0:
    print(i)
    i-=1
    '''
'''
i=2
while i<=100:
    print(i,end=' ')
    i+=2
    '''
s = 'python programming'

'''
i = len(s)-1
while i>=0:
    print(s[i],end='')
    i-=1
    '''
'''
l =[1,0,0,0,2,3,4,5,6,12,34,14,0,76,0]
while 0 in l:
    l.remove(0)

print(l)
'''
'''
data = {}
total_bill = 0
while True:
    product = input("Enter the product(for exit): ")
    if product == 'exit':
        break
    price = int(input("Enter the price: "))
    total_bill+=price
    data[product] = price

print(data)
print("Total Bill:",total_bill)
'''

'''
i=0
while i<=10:
    i+=1
    if i==15:
        break
    print(i)
else:
    print("End of the loop")
    '''

