'''
class whatsappV1:
    def __init__(self,name):
        self.name = name
        print(f"welcome to the whatsapp - v1 {self.name}!")
    def messaging(self):
        print("you can send messages")

class whatsappsV2(whatsappV1):
    def __init__(self,name):
            self.name = name
            print(f"Welcome to the whatsapp - v2 {self.name}!")
    def calls(self):
        print("You can audio and video calls")

sajid = whatsappsV2('sajid')
sajid.messaging()

Teju = whatsappsV2('Teju')
Teju.messaging()

Kavya = whatsappsV2('Kavya')
Kavya.messaging()
Kavya.calls()
'''

