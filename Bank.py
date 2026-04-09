class BankAccount:
     def __init__(self,name,pin):
             self.name = name
             self.pin = pin
     def changePin(self):
             old_pin = int(input("Enter current Pin: "))
             if old_pin == self.pin:
                 new_pin = int(input("Enter new Pin: "))
                 self.pin = new_pin
                 print("PIN chnaged Successfully")
             else:
                 print("Incorrect PIN")

a = BankAccount("Disha",93)
a.changePin()
