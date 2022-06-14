#creating python atm for account balance, withdraw and deposit of money. WISH ME LUCK!


import random

class AtmAcct:
    def __init__ (self, identity, balance2 = 0, annualrate = 2.5):
        self.identity = identity
        self.balance2 = balance2
        self.rate = annualrate

def getidentity(self):
    return self.identity

def deposit(self, amount):
    self.balance2 += amount
def withdraw(self, amount):
    self.balance -= amount 
def getblance2(self):
    return self.balance2

def getannualrate(self):
    return self.annualrate
def getmonthrate(self):
    return self.annualrate / 12
def getmonth(self):
    return self.balance2 * self.getmonthrate()


def main():
    #creatng the accounts
    accounts= []
    for i in range(1000, 9999):
        account  = AtmAcct(i, 0)
        accounts.append(account)
    
    
    while True:
        identity = int(input("Please enter your pin : "))
        while identity < 1000 or id > 9999:
            identity = int(input("Invalid pin! Re-enter pin : "))
        
        while True:
            print("\n[1]. View balance \t [2] Withdraw \t [3] Deposit \t [4] Exit ")

            option = int(input("Select your option"))

            for acc in accounts:
                if acc.getidentity() == identity:
                    AtmAcctsub = acc
                    break


            if option == 1:
                print(AtmAcctsub.getbalance2())
            
            elif option == 2:
                amt = float(input("Enter amount to withdraw: "))
                plusans = input("Confirm this entry with Yes or No ? " + str(amt) + " ")
                if plusans == "Yes":
                    print("Verified withrawal")
                else:
                    break


                if amt < AtmAcctsub.getbalance2():
                    AtmAcctsub.withdraw(amt)
                    print("Your new balance: " + str(AtmAcctsub.getbalance2()) + "n ")
                else:
                    print("You have insufficient balance : " + str(AtmAcctsub.getbalance2()) + " n")


            elif option == 3:
                amt = float(input("Please enter amount to deposit: "))
                depoans = input("Confirm entry with Yes or No ? " + str(amt) + " ")

                if depoans == "Yes":
                    AtmAcctsub.deposit(amt)
                    print("Current balance: " + str(AtmAcctsub.getbalance2()) + " n")
                else:
                    break

            elif option == 4:
                print("Transaction successful")
                print("Transaction no :", random.randint(1000, 1000000))
                print("current interest rate : ", AtmAcctsub.annualrate)
                print("monthly interest rate :", AtmAcctsub.annualrate /12)
                print("THANK YOU!")

            else:
                print("Invalid option. ")

main()



    

