# Write a program to create an atm simulation

balance = 0.00
while True:
    print("\n\n------------------------------------\nWelcome to our ATM")
    print("Please select an option ")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Check Balance")
    print("4. Exit")

    n = int(input("Enter your choice: "))
    if n == 1:
        withdraw = float(input("\nEnter amount to withdraw: "))
        if withdraw > balance:
            print("Insufficient balance")
        else:
            balance -= withdraw
            print(f"You have withdrawn ₹{withdraw:.2f}")
            print(f"\nYour balance is ₹{balance:.2f}")
            print("Thank you for using our service\n")
    elif n == 2:
        dep = float(input("\nEnter the amount to deposit: "))
        balance += dep
        print(f"You have deposited ₹ {dep:.2f}")
        print(f"Your balance is ₹ {balance}")
        print("Thank you for using our service\n")
    elif n == 3:
        print(f"\nYour balance is ₹ {balance:.2f}")
        print("Thank you for using our service\n")
    elif n == 4:
        print("Exit")
        break
    else:
        print("Invalid choice")
    
    input("Press enter to continue...")
