#int float str list tuple set dict bool

#int float str tuple bool
#list set dict


def display(n):
    n[5]=6
    print("Inside:",n)

n={1:2,3:4}
display(n)
print('Outside:',n)