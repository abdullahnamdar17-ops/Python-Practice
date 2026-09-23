# class student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def average(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print(f"Average marks of, {self.name}, is, {sum / 3}")

# s1 = student("shabs", [90, 80, 70])
# s1.average()

class Account:
    def __init__(self, balance, accNo):
        self.balance = balance
        self.accNo = accNo
    
    @staticmethod
    def hello():
        print("Hello, welcome to the bank")

    def debit(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Debited {amount} from acc number {self.accNo}. Remaining balace is {self.balance}")
    def credit(self, amount):
        self.balance += amount
        print(f"Credited USD {amount} in your account {self.accNo}, New balance is USD {self.balance}")

s1 = Account(1000, "PK123456")
s1.hello()
s1.debit(5000)
s1.debit(500)
s1.credit(1000)
