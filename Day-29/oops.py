'''class Flipkart:
    products={'shirts':1000,'handbag':2000,'pants':3000}
    discount=30

    @classmethod
    def display(cls):
        print(cls.products)
    def userinfo(self,name,phone,address):
        self.name=name
        self.phone=phone
        self.address=address
        print(f"Hello {self.name},Welcome to the flipkart")

    @staticmethod
    def displaydiscount():
        print(f"{Flipkart.discount}% discount is going-on,grab the products...")
david=Flipkart()
david.userinfo('david',9978456102,'Hyd')
david.displaydiscount()
david.display()
jack=Flipkart()
jack.userinfo('jack',8899774411,'chennai')
jack.displaydiscount()
jack.display()
alex=Flipkart()
alex.userinfo('alex',8877552101,'guntur')
alex.displaydiscount()
alex.display()'''

class User:
    def __init__(self, name, email, phone, password):
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password

    def register(self):
        if not self.name:
            print("Registration failed: Name is required")
        elif not self.email:
            print("Registration failed: Email is required")
        elif not self.phone:
            print("Registration failed: phone is required")
        elif not self.password:
            print("Registration failed: password is required")
        else:
            print("Registration successful")

User1 = User("teju", "teju@gmail.com", "9515626942", "teju@123")
User1.register()

User2 = User("teju", "", "9515626942", "teju@123")
User2.register()
