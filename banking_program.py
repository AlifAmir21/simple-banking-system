# Python Banking Program

def show_balance(balance, name):
    print(f"{name}, your balance is RM {balance:.2f}")

def deposit():
    amount = float(input("Enter the amount to deposit: RM "))

    if amount < 0:
        print ("That's not a valid amount. Please enter a reasonable amount to deposit.")
        return 0
    else:
      return amount

def withdraw(balance):
    amount = float(input("Enter the amount to withdraw: RM "))

    if amount > balance:
        print ("Insufficient funds. Please enter an amount less than or equal to your balance.")
        return 0
    elif amount < 0:
        print ("Amount must be greater than zero") 
        return 0
    else:
        return amount

def main():
    print ("Welcome to the Banking Program!")
    name = input("Please enter your name: ")
    print (f"Hello {name}, Let's get started with your banking needs.")
    balance = 0
    is_running = True

    while is_running:
        print ("***********************************")
        print ("    Welcome to Banking Program    ")
        print ("***********************************")
        print ("1. Show Balance")
        print ("2. Deposit")   
        print ("3. Withdraw")
        print ("4. Exit")
        print ("***********************************")

        choice = input ("Please enter your choice (1-4): ")
        
        if choice == '1':
            show_balance(balance, name)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
        
            print ("Invalid choice. Please try again.")
            
    print ("*************************************************")
    print ("Thank you for using the Banking Program. Goodbye!")
    print ("*************************************************") 
if __name__ == "__main__":
    main()  

