"""
BANKING SYSTEM – CORRECTED VERSION
Method Overloading simulated with default parameters.
"""

import datetime

# ============================================================
# ACCOUNT DATABASE
# ============================================================

class Account:
    def __init__(self, number, holder, balance=0.0):
        self.number = number
        self.holder = holder
        self.balance = balance

BANK = {
    "EMP-001": Account("EMP-001", "Kirabo Eria", 5000.00),
    "SAV-001": Account("SAV-001", "Kirabo Eria", 2000.00),
    "EMP-002": Account("EMP-002", "Sarah Smith", 3000.00),
}

def find_account(number):
    return BANK.get(number)

def update_balance(number, new_balance):
    acc = find_account(number)
    if acc:
        acc.balance = new_balance
        return True
    return False

# ============================================================
# PARENT CLASS – Transaction
# ============================================================

class Transaction:
    def __init__(self, amount, description=""):
        self.amount = amount
        self.description = description
        self.status = "Pending"
        self.timestamp = None
        self.tx_id = None

    # ==========================================================
    # METHOD OVERLOADING SIMULATION (single method with defaults)
    # ==========================================================

    def process_transaction(self, fee=0.0, callback=None):
        """
        Simulates overloading by accepting optional fee and callback.
        Can be called as:
          - process_transaction()
          - process_transaction(fee=5.0)
          - process_transaction(fee=5.0, callback=notify)
        """
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.tx_id = f"TX-{hash(self.timestamp)}"

        if fee > 0:
            print(f"💰 Processing ${self.amount:.2f} (fee: ${fee:.2f})")
        else:
            print(f"💰 Processing ${self.amount:.2f}")

        self.status = "Completed"
        if callback:
            callback(self)

    # ==========================================================
    # METHOD TO BE OVERRIDDEN
    # ==========================================================

    def validate_transaction(self):
        if self.amount <= 0:
            print("❌ Amount must be greater than 0")
            return False
        return True

# ============================================================
# CHILD CLASSES – Method Overriding
# ============================================================

class Deposit(Transaction):
    def __init__(self, amount, account_number, description="Deposit"):
        super().__init__(amount, description)
        self.account_number = account_number

    # ---- OVERRIDING ----
    def validate_transaction(self):
        acc = find_account(self.account_number)
        if not acc:
            print(f"❌ Account {self.account_number} not found")
            return False
        if self.amount <= 0:
            print("❌ Amount must be greater than 0")
            return False
        return True

    def process_transaction(self, fee=0.0, callback=None):
        if not self.validate_transaction():
            self.status = "Failed"
            return False

        acc = find_account(self.account_number)
        new_balance = acc.balance + self.amount
        update_balance(self.account_number, new_balance)

        super().process_transaction(fee, callback)

        print(f"✅ ${self.amount:.2f} deposited")
        print(f"   New balance: ${new_balance:.2f}")
        return True


class Withdrawal(Transaction):
    def __init__(self, amount, account_number, description="Withdrawal"):
        super().__init__(amount, description)
        self.account_number = account_number
        self.balance_after = 0

    # ---- OVERRIDING ----
    def validate_transaction(self):
        acc = find_account(self.account_number)
        if not acc:
            print(f"❌ Account {self.account_number} not found")
            return False
        if self.amount <= 0:
            print("❌ Amount must be greater than 0")
            return False
        if self.amount > acc.balance:
            print(f"❌ Insufficient balance. Available: ${acc.balance:.2f}")
            return False
        self.balance_after = acc.balance - self.amount
        return True

    def process_transaction(self, fee=0.0, callback=None):
        if not self.validate_transaction():
            self.status = "Failed"
            return False

        update_balance(self.account_number, self.balance_after)

        super().process_transaction(fee, callback)

        print(f"✅ ${self.amount:.2f} withdrawn")
        print(f"   New balance: ${self.balance_after:.2f}")
        return True


class Transfer(Transaction):
    def __init__(self, amount, from_account, to_account, description="Transfer"):
        super().__init__(amount, description)
        self.from_account = from_account
        self.to_account = to_account
        self.from_balance_after = 0
        self.to_balance_after = 0

    # ---- OVERRIDING ----
    def validate_transaction(self):
        if self.amount <= 0:
            print("❌ Amount must be greater than 0")
            return False

        from_acc = find_account(self.from_account)
        if not from_acc:
            print(f"❌ Source account {self.from_account} not found")
            return False

        to_acc = find_account(self.to_account)
        if not to_acc:
            print(f"❌ Destination account {self.to_account} not found")
            return False

        if self.from_account == self.to_account:
            print("❌ Cannot transfer to same account")
            return False

        if self.amount > from_acc.balance:
            print(f"❌ Insufficient balance. Available: ${from_acc.balance:.2f}")
            return False

        self.from_balance_after = from_acc.balance - self.amount
        self.to_balance_after = to_acc.balance + self.amount
        return True

    def process_transaction(self, fee=0.0, callback=None):
        if not self.validate_transaction():
            self.status = "Failed"
            return False

        update_balance(self.from_account, self.from_balance_after)
        update_balance(self.to_account, self.to_balance_after)

        super().process_transaction(fee, callback)

        print(f"✅ ${self.amount:.2f} transferred")
        print(f"   Source balance: ${self.from_balance_after:.2f}")
        print(f"   Destination balance: ${self.to_balance_after:.2f}")
        return True

# ============================================================
# CALLBACK FUNCTION
# ============================================================

def send_notification(tx):
    print(f"   📧 {tx.description} – {tx.status} (ID: {tx.tx_id})")

# ============================================================
# MENU (same as before)
# ============================================================

def display_accounts():
    print("\n" + "="*60)
    print("   📋 AVAILABLE ACCOUNTS")
    print("="*60)
    for acc in BANK.values():
        print(f"   {acc.number} | {acc.holder} | ${acc.balance:.2f}")
    print("="*60)

def main():
    print("\n" + "="*60)
    print("   🏦 WELCOME TO SIMPLE BANKING SYSTEM")
    print("="*60)

    while True:
        print("\n" + "="*40)
        print("   BANKING MENU")
        print("="*40)
        print("1. View Accounts")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Check Balance")
        print("6. Exit")
        print("="*40)

        choice = input("Choose (1-6): ").strip()

        if choice == "1":
            display_accounts()

        elif choice == "2":
            print("\n--- DEPOSIT ---")
            acc = input("Account number: ").strip().upper()
            if not find_account(acc):
                print("❌ Account not found")
                continue
            try:
                amount = float(input("Amount: $"))
            except ValueError:
                print("❌ Invalid amount")
                continue
            fee = input("Apply fee? (yes/no): ").strip().lower()
            deposit = Deposit(amount, acc, "Deposit")
            if fee == "yes":
                deposit.process_transaction(fee=5.00, callback=send_notification)
            else:
                deposit.process_transaction()   # <-- overloading: no fee

        elif choice == "3":
            print("\n--- WITHDRAWAL ---")
            acc = input("Account number: ").strip().upper()
            if not find_account(acc):
                print("❌ Account not found")
                continue
            try:
                amount = float(input("Amount: $"))
            except ValueError:
                print("❌ Invalid amount")
                continue
            fee = input("Apply ATM fee? (yes/no): ").strip().lower()
            withdrawal = Withdrawal(amount, acc, "Withdrawal")
            if fee == "yes":
                withdrawal.process_transaction(fee=2.50, callback=send_notification)
            else:
                withdrawal.process_transaction()

        elif choice == "4":
            print("\n--- TRANSFER ---")
            from_acc = input("From account: ").strip().upper()
            if not find_account(from_acc):
                print("❌ Source account not found")
                continue
            to_acc = input("To account: ").strip().upper()
            if not find_account(to_acc):
                print("❌ Destination account not found")
                continue
            if from_acc == to_acc:
                print("❌ Cannot transfer to same account")
                continue
            try:
                amount = float(input("Amount: $"))
            except ValueError:
                print("❌ Invalid amount")
                continue
            fee = input("Apply transfer fee? (yes/no): ").strip().lower()
            transfer = Transfer(amount, from_acc, to_acc, "Transfer")
            if fee == "yes":
                transfer.process_transaction(fee=10.00, callback=send_notification)
            else:
                transfer.process_transaction()

        elif choice == "5":
            print("\n--- CHECK BALANCE ---")
            acc = input("Account number: ").strip().upper()
            account = find_account(acc)
            if account:
                print(f"\n👤 {account.holder}")
                print(f"🏦 {account.number}")
                print(f"💰 ${account.balance:.2f}")
            else:
                print("❌ Account not found")

        elif choice == "6":
            print("\n👋 Thank you for using the banking system!")
            break

        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    main()