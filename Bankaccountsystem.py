# Bank Account System
class BankAccount:
    # Class Attribute
    bank = "absa"

    def __init__(self, name, money):
        self.name = name
        self.money = money
        
    def balance(self):
            return f'You have ${self.money:,} left in your account'
    
    # Instance method Deposite
    def deposite(self, cash):
        self.money = self.money + cash
        return f'You deposite ${self.money:,} to your account'

    # Instance method Withdrawal
    def withdraw(self, cash):
        self.money = self.money - cash
        if self.money == 0:
           print("You have no money in your account")
        elif self.money < cash:
            print("You have less money in your account")
        else:
            print(f"You withdrew ${self.money:,} from your account")

    
    
