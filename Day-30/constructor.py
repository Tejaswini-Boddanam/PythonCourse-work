
'''class Flipkart:
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone
        print(f"Hello {self.name}, Welcome to the flipkart")

Teju = Flipkart('Teju',9876543210)
kavya = Flipkart('kavya',9876543210)
pavani = Flipkart('pavani',9876543210)
'''

'''class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.__password = password
        self._posts = []

    def getpassword(self):
        return self.__password

    def setpassword(self,newpassword):
        self.__password = newpassword

    @property
    def accesspost(self):
        return self._posts

    @accesspost.setter
    def accesspost(self,newpost):
        self._posts.append(newpost)


    def display(self):
        print(self.username,self.__password,self._posts)


kavya = Instagram('kavya','kavya@123')
kavya.display()
print(kavya.username)
print(kavya.getpassword())
print(kavya.accesspost)

kavya.username = 'panny'
kavya.setpassword("panny@123")
kavya.accesspost = "sunrise.png"
kavya.accesspost = "beach.png"
kavya.accesspost = "forest.png"'''
