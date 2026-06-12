"""
E-COMMERCE CHECKOUT SYSTEM
Assignment 2 - Login System with Roles & Nested Conditions
Student: Kirabo Eria
"""

print("\n" + "="*60)
print("     WELCOME TO SHOPPY CHECKOUT")
print("="*60)

# ============================================================
# DATABASES
# ============================================================

# User database
users = {
    "admin": {"password": "admin123", "role": "Admin"},
    "cashier_jane": {"password": "cash456", "role": "Cashier"},
    "eria_k": {"password": "eria123", "role": "Customer"},
    "john_customer": {"password": "john123", "role": "Customer"}
}

# Coupon database
coupons = {
    "WELCOME10": {"discount": 10, "min_spend": 0},
    "SAVE20": {"discount": 20, "min_spend": 100},
    "FLASH50": {"discount": 50, "min_spend": 200},
    "STUDENT15": {"discount": 15, "min_spend": 50}
}

# Tax rates
tax_rates = {
    "CA": 0.085,
    "NY": 0.08875,
    "TX": 0.0625,
    "FL": 0.07,
    "OTHER": 0.05
}

# ============================================================
# LOGIN SYSTEM
# ============================================================

print("\n--- LOGIN ---")

max_attempts = 3
attempts = 0
logged_in = False
user_role = None
current_user = None

while attempts < max_attempts and not logged_in:
    print(f"\nAttempt {attempts + 1} of {max_attempts}")
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    
    if username in users and users[username]["password"] == password:
        logged_in = True
        user_role = users[username]["role"]
        current_user = username
        print(f"\n Login successful! Welcome, {username}")
        print(f"   Role: {user_role}")
    else:
        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f" Invalid credentials. {remaining} attempts left.")
        else:
            print(" Too many failed attempts. Access denied.")
            exit()

print("\n" + "="*60)
print(f"ACCESS LEVEL: {user_role}")
print("="*60)

# ============================================================
# PRICE CALCULATION
# ============================================================

print("\n" + "="*60)
print("     CHECKOUT")
print("="*60)

# Input subtotal
while True:
    try:
        subtotal = float(input("\n Enter subtotal amount: $"))
        if subtotal <= 0:
            print(" Amount must be positive.")
            continue
        break
    except ValueError:
        print(" Please enter a valid number.")

# ============================================================
# COUPON VERIFICATION
# ============================================================

print("\n--- COUPON ---")
coupon_code = input("Enter coupon code (or press Enter to skip): ").strip().upper()

discount_amount = 0
discount_percent = 0

if coupon_code:
    if coupon_code in coupons:
        if subtotal >= coupons[coupon_code]["min_spend"]:
            discount_percent = coupons[coupon_code]["discount"]
            discount_amount = subtotal * (discount_percent / 100)
            print(f"\n Coupon '{coupon_code}' applied!")
            print(f"   {discount_percent}% discount - ${discount_amount:.2f}")
        else:
            min_needed = coupons[coupon_code]["min_spend"]
            print(f"\n Coupon requires ${min_needed} minimum spend.")
            print(f"   Add ${min_needed - subtotal:.2f} more.")
    else:
        print(f"\n '{coupon_code}' is not a valid coupon.")
else:
    print("\n No coupon applied.")

after_discount = subtotal - discount_amount

# ============================================================
# TAX CALCULATION
# ============================================================

print("\n--- TAX ---")
print("Locations: CA (8.5%), NY (8.875%), TX (6.25%), FL (7.0%)")
location = input("Enter location: ").strip().upper()

if location in tax_rates:
    tax_rate = tax_rates[location]
    print(f" Tax rate: {tax_rate * 100}%")
else:
    tax_rate = tax_rates["OTHER"]
    print(f" Default tax rate: {tax_rate * 100}%")

tax_amount = after_discount * tax_rate
final_price = after_discount + tax_amount

# ============================================================
# LOYALTY TIERS
# ============================================================

print("\n--- LOYALTY DISCOUNT ---")

loyalty_discount = 0

if subtotal >= 500:
    loyalty_discount = after_discount * 0.05
    print(f" Premium tier: 5% off (-${loyalty_discount:.2f})")
elif subtotal >= 200:
    loyalty_discount = after_discount * 0.03
    print(f" Gold tier: 3% off (-${loyalty_discount:.2f})")
elif subtotal >= 100:
    loyalty_discount = after_discount * 0.01
    print(f" Silver tier: 1% off (-${loyalty_discount:.2f})")
else:
    print(f" Basic tier: No loyalty discount")
    print(f"   Spend ${100 - subtotal:.2f} more for 1% off")

after_loyalty = after_discount - loyalty_discount
tax_amount = after_loyalty * tax_rate
final_price = after_loyalty + tax_amount

# ============================================================
# RECEIPT
# ============================================================

print("\n" + "="*60)
print("                     RECEIPT")
print("="*60)
print(f"{'Customer:':<20} {current_user} ({user_role})")
print("-"*60)
print(f"{'Subtotal:':<20} ${subtotal:>12.2f}")

if discount_amount > 0:
    print(f"{'Coupon discount:':<20} -${discount_amount:>11.2f}")
    print(f"{'Coupon used:':<20} {coupon_code}")

if loyalty_discount > 0:
    print(f"{'Loyalty discount:':<20} -${loyalty_discount:>11.2f}")

print(f"{'After discounts:':<20} ${after_loyalty:>12.2f}")
print(f"{'Tax rate:':<20} {tax_rate * 100:>11.1f}%")
print(f"{'Tax amount:':<20} ${tax_amount:>12.2f}")
print("="*60)
print(f"{'TOTAL DUE:':<20} ${final_price:>12.2f}")
print("="*60)

# Savings
total_saved = discount_amount + loyalty_discount
if total_saved > 0:
    print(f"\n You saved ${total_saved:.2f} today!")

# ============================================================
# ROLE-SPECIFIC ACTIONS
# ============================================================

print("\n" + "="*60)

if user_role == "Admin":
    print("\n ADMIN ACCESS")
    print("-"*30)
    print("+ Process transactions (completed above)")
    print("+ View registered users")
    print("+ View coupons")
    
    admin_choice = input("\nView registered users? (yes/no): ").strip().lower()
    
    if admin_choice == "yes":
        print("\n REGISTERED USERS:")
        for user, info in users.items():
            print(f"   . {user} ({info['role']})")
    
    view_coupons = input("\nView available coupons? (yes/no): ").strip().lower()
    
    if view_coupons == "yes":
        print("\n AVAILABLE COUPONS:")
        for code, info in coupons.items():
            print(f"   . {code}: {info['discount']}% off (min ${info['min_spend']})")
    
    print("\n Admin session complete.")

elif user_role == "Cashier":
    print("\n CASHIER: Transaction completed and logged.")
    print("   Next customer please!")

elif user_role == "Customer":
    print("\n CUSTOMER: Thank you for shopping at Shoppy!")
    if total_saved > 0:
        print(f"   You saved ${total_saved:.2f} today!")

# ============================================================
# END
# ============================================================

print("\n" + "="*60)
print("     THANK YOU FOR USING SHOPPY")
print("="*60)