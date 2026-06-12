# BILL SPLIT CALCULATOR
print("\n" + "="*40)
print("     BILL SPLIT CALCULATOR")
print("="*40 + "\n")

# 1. GET INPUTS WITH VALIDATION
while True:
    try:
        total_bill = float(input("Enter total bill amount: $"))
        if total_bill <= 0:
            print("Bill amount must be positive. Try again.\n")
            continue
        break
    except ValueError:
        print("Please enter a valid number.\n")

while True:
    try:
        num_people = int(input("👥 Enter number of people: "))
        if num_people <= 0:
            print("Must have at least 1 person. Try again.\n")
            continue
        break
    except ValueError:
        print("Please enter a valid whole number.\n")

# Tip percentage options
print("\n💡 Tip options: 10%, 15%, 20%, or custom")
while True:
    tip_choice = input("Choose tip percentage (10/15/20/custom): ").strip().lower()
    
    if tip_choice == "custom":
        while True:
            try:
                tip_percent = float(input("Enter custom tip percentage: "))
                if tip_percent < 0:
                    print("Tip cannot be negative.\n")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.\n")
        break
    elif tip_choice in ["10", "15", "20"]:
        tip_percent = float(tip_choice)
        break
    else:
        print("Please choose 10, 15, 20, or custom.\n")

# 2. CALCULATIONS
tip_amount = total_bill * (tip_percent / 100)
total_with_tip = total_bill + tip_amount
per_person = total_with_tip / num_people

# 3. FORMATTED RECEIPT OUTPUT
print("\n" + "="*45)
print("            RECEIPT")
print("="*45)
print(f"{'Bill amount:':<20} ${total_bill:>10.2f}")
print(f"{'Tip (' + str(int(tip_percent)) + '%):':<20} ${tip_amount:>10.2f}")
print("-"*45)
print(f"{'Total with tip:':<20} ${total_with_tip:>10.2f}")
print(f"{'Number of people:':<20} {num_people:>10}")
print("="*45)
print(f"{'Each person pays:':<20} ${per_person:>10.2f}")
print("="*45 + "\n")

