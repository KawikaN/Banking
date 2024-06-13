from mysite.Accounts.accounts import *
from mysite.linkedList import *


accessable = 0






accessable = Account.availableFunds


print(accessable)
# print(Mokihana)
# print(accessable)



# A = LinkedList()
# A.insertAtEnd('a')
# A.insertAtEnd('b')
# A.insertAtEnd('c')

# A.printLL()

x=0
users = []
passwords = []
emails = []
numbers = []
addresses = []


while (input("Do you want to add more users(y/n) ") == "y"):
    users.append(input("Enter your name ").lower())
    passwords.append(input("Enter your password "))
    emails.append(input("Enter your email "))
    numbers.append(input("Enter your number "))
    addresses.append(input("Enter your address "))

    x = x + 1


for x in range(len(users)):
    objs = [Checkings("silver", users[x], passwords[x], emails[x], numbers[x], addresses[x])] # list of users
# for users in objs:

print(objs[0])
while True:
    currentUser = -1
    accountName = input("enter name of the account ")
    for i in range(len(objs)):
        if(objs[i].getName() == accountName):
            currentUser = i
        elif(objs[i].getName() == accountName.lower()):
            currentUser = i
    if(currentUser == -1):
        print(objs[i].getName())
        print(accountName)
        print("user not found")
        continue
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