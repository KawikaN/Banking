from accounts import *
from linkedList import *
accessable = 0

A1 = Checkings("silver", "Password", "email@gmail.com", "8084764794", "89-1206 Pikaiolena St.")
A2 = Savings("silver", "Password", "email@gmail.com", "8084764794", "89-1206 Pikaiolena St.",)
Mokihana = Savings("silver", "Cupcake", "mokihanapaik@gmail.com", "8087822974", "45-389 Waikua Pl")
James = Savings("silver", "Cupcake", "mokihanapaik@gmail.com", "8087822974", "45-389 Waikua Pl")






print(Mokihana.withdraw(100))
Mokihana.deposit(100)
James.deposit(100)


accessable = Account.availableFunds


print(accessable)
# print(Mokihana)
# print(accessable)



A = LinkedList()
A.insertAtEnd('a')
A.insertAtEnd('b')
A.insertAtEnd('c')

A.printLL()

x=0
users = []
passwords = []
emails = []
numbers = []
addresses = []


while (input("Do you want to add more users(y/n) ") == "y"):
    users.append(input("Enter your name "))
    passwords.append(input("Enter your password "))
    emails.append(input("Enter your email "))
    numbers.append(input("Enter your number "))
    addresses.append(input("Enter your address "))

    x = x + 1


for x in range(len(users)):
    print(x)
    objs = [Checkings("silver", passwords[x], emails[x], numbers[x], addresses[x])] # list of users
# for users in objs:

while True:
    currentUser = 0
    accountName = input("enter name of the account ")    
    try:
        for i in range(len(objs)):
            if(objs[i] == accountName):
                currentUser = i
            elif(objs[i] == accountName.lower()):
                currentUser = i
    except:
        print("User not found")

    choice = int(input('Do you want to-\nmake a deposite (0): \nmake a withdraw (1)\ncheck your balance (2)\nor view your account info (3)\n'))
    
    try:
        if(choice == 0):
            amount = int(input("How much do you want to deposit? "))
            print(objs[currentUser].deposit(amount))
        elif(choice == 1):
            amount = int(input("How much do you want to withdraw? "))
            print(objs[currentUser].withdraw(amount))
        elif(choice == 2):
            print(objs[currentUser])
        elif(choice == 3):
            print(objs[currentUser].Data())
    except:
        print("You did not select a valid option")
    



# for x in users:
#     users[x]
print(objs[0])