card_number = input ("Please insert your card number :- ")
pin_number = input ("Enter pin number :- ")
print("Please choose activity")
print("Enter 1 for balance enquiry")
print("Enter 2 for WithDawal")
option = input("Enter :- ")
balance = 5000
i = 0

while i < 1:
    if int(option) == 1:
        print("Your balance is $5000")
        break
    elif int(option) == 2:
        amount = input ("Enter amount of withdawal :- ")
        if int(amount) > balance:
            print(f"Sorry you don't have enough credit you balance is {balance}")
            break
        elif int(amount) < balance:
            print(f"You have successfully withdawal amount {amount}. your remaining balance is {balance - int(amount)} ")
        break
    else:
        print("Number is invalid")
        break
        