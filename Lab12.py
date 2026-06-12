bank_balance = 1000
while(bank_balance):
    amount=int(input("Enter amount to withdraw: "))
    amountin=int(input("Enter amount to deposit: "))
    if amount>bank_balance:
        print("Insufficient funds. Please enter a valid amount.")
        
    else:
        bank_balance=bank_balance-amount
        bank_balance=bank_balance+amountin
        print(f"Your new balance is: ${bank_balance}")
        