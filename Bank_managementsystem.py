#create a class Bank with methods deposit and withdraw

class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def check_balance(self):
        print (f"Acc Name:  {self.name}")
        print (f"Balance:   {self.balance}")

    def withdraw(self, with_amount ):
        if with_amount > 0 :
            if with_amount < self.balance:
                self.balance -= with_amount
                print (f"Withdrew :             {with_amount}")
                print (f"Remaining Balance :    {self.balance}")
            
            else:
                print ("Not enough Balance!")

        else:
            print ("Enter Valid amount!")

    def deposit (self, dep_amount):
        if dep_amount > 0 :
            self.balance += dep_amount
            print (f"Amount Deposited :     {dep_amount}")
            print (f"Updated Balance :      {self.balance}")
        else:
            print ("Enter a valid amount!")

account = Bank("ABC", 1000.00)
while True:
    print ("\n 1. Check balance \n 2. Wtihdraw \n 3. Deposit \n 4. Exit")
    choice = int(input("Enter your choice:  "))

    if choice == 1:
        account.check_balance()

    elif choice == 2:
        withdraw_amt = float(input("Enter amount to Withdraw:   "))
        account.withdraw(withdraw_amt)

    elif choice == 3:
        deposit_amt = float(input("Enter amount to deposit:   "))
        account.deposit(deposit_amt)

    elif choice == 4:
        print("Exiting.")
        break

    else:
        print("Invalid!")
