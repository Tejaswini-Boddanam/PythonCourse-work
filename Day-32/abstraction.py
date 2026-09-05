'''
from abc import ABC,abstractmethod

class phonepay(ABC):

    def senderinfo(self):
        print("You can enter their mobile number or scanner")
    def amount(self):
        print("You can enter amount")
    def pin(self):
        print("You need to enter the pin")

    @abstractmethod
    def transaction(self):
        pass

class HDFC(phonepay):
    def transaction(self):
        print("payment using hdfc bank")

class SBI(phonepay):
    def transaction(self):
        print("payment using sbi bank")

class UNION(phonepay):
    def transaction(self):
        print("payment using union bank")

class ICIC(phonepay):
    def transaction(self):
        print("payment using icic bank")

class AXIS(phonepay):
    def transaction(self):
        print("payment using axis bank")

Teju = HDFC()
Teju.senderinfo()
Teju.amount()
Teju.pin()
Teju.transaction()

Deepu = SBI()
Deepu.senderinfo()
Deepu.amount()
Deepu.pin()
Deepu.transaction()

kavya = ICIC()
kavya.senderinfo()
kavya.amount()
kavya.pin()
kavya.transaction()

pavani = UNION()
pavani.senderinfo()
pavani.amount()
pavani.pin()
pavani.transaction()

sathwika = AXIS()
sathwika.senderinfo()
sathwika.amount()
sathwika.pin()
sathwika.transaction()
'''








