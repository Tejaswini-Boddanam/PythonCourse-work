'''
class whatsappv1:
    def messaging(self):
        print("You can message")

class whatsappv2:
    def extramessage(self):
        print("You can add emojis,stickers and gifs")

class whatsappv3(whatsappv1,whatsappv2):
    def calls(self):
        print("You can audio and video calls")

class whatsappv4(whatsappv3):
    def status(self):
        print("You can add status for 24 hours")

a=whatsappv1()
a.messaging()

b=whatsappv2()
b.extramessage()
#b.calls()

c=whatsappv3()
c.messaging()
c.calls()
c.extramessage()

d=whatsappv4()
d.messaging()
d.calls()
d.extramessage()
d.status()
'''
