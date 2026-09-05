'''
#positive or negative number
n = int(input("Enter a number: "))
if n>0:
    print("The number is positive")
elif n<0:
    print("The number is negative")
    '''
#even or odd number
'''
n = int(input("Enter a number: "))
if n%2==0:
    print("The number is even")
else:
    print("The number is odd")
    '''
#Divisible by 5
'''
n = int(input("Enter a number: "))
if n%5==0:
    print("The number is divisible by 5")
else:
    print("The number is not divisible by 5")
    '''
#Divisibility by 5 and 11
'''
n = int(input("Enter a number: "))
if n%5==0 and n%11==0:
    print("The number is divisible by 5 and 11")
else:
    print("The number is not divisible by 5 and 11")
    '''


'''
seat_type = input()
booking_days = int(input())
festival = input()
age = int(input())
price = 5000
if seat_type == "Economy":
    price = price + (price * 40/100)
elif seat_type == "premium economy":
    price = price + (price * 20/100)
if booking_days > 30:
    price = price -(price  * 10/100)
elif booking_days < 7:
    price = price + (price * 25/100)
if festival == "True":
    price = price + (price * 20/100)
if age > 60:
    price = price - (price * 15/100)

print("Final Ticket price:", price)'''


age = int(input("Enter the age:"))
health_score = int(input("Enter the health_score:"))
veh_type = input("Enter the vehicle type:")
Base_premium = 10000
if age < 25:
    Base_premium *= 1.2
elif age > 50:
    Base_premium *= 1.15

if health_score >= 80:
    Base_premium *= 0.9
elif health_score < 60:
    Base_premium *= 1.2

if veh_type == "sports car":
    Base_premium *= 1.3

elif veh_type == "SUV":
    Base_premium *=1.15

print(Base_premium)





