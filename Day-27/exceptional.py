'''
try:
    #a = int(input())
    k={1:12,12:13}
    #print(k[14])
    l=[232,54]
    #print(l[10])
    #print(10/0)
    #print('l'+1)
except ValueError:
    print("Enter the correct datatype")
except KeyError:
    print("key is not there")
except IndexError:
    print("Index out of range")
except ZeroDivisionError:
    print("can't divide with zero")
except TypeError:
    print("Enter the correct datatype")
except NameError:
else:
    print("a=",a)
finally:
    print("End of the program")'''

'''
try:
    # a = int(input())
    k ={1:12,12:13}
    #print(k[14])
    l=[232,54]
    #print(l[10])
    #print(10/0)
    #print('l+1)
except (ValueError,KeyError,IndexError,ZeroDivisionError,TypeError,NameError) as e:
    print("Error occured:",e)
else:
    print("Error free program")
finally:
    print("End of the program")
    '''


'''try:
    # a = int(input("Enter: "))
    k ={1:12,12:13}
    #print(k[14])
    l=[232,54]
    #print(l[10])
    #print(10/0)
    #print('l+1)
except Exception as e:
    print("Error occured:",e)
else:
    print("Error free program")
finally:
    print("End of the program")'''

try:
    amount =int(input("Enter the amount:"))
    balance = 5000
    if balance < 0:
    raise Exception("Amount needs to be positive")
except Exception as e:
    print("Error occured:",e)
else:
    print("Error free program")
finally:
    print("End of the program")