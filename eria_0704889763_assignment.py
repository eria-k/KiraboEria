"""
CONTACT MANAGEMENT SYSTEM
Features:
- CRUD Operations (Create, Read, Update, Delete)
- Data Validation (Phone & Email)
- Advanced Search (Name, Phone, Email)
- Interactive CLI Menu
"""

import re

# ============================================================
# DATA VALIDATION
# ============================================================

class ContactManager:
    """
    A class to manage contacts with validation and search functionality.
    """
    
    def __init__(self):
        """Initialize the contact manager with an empty list."""
        self.contacts = []
    
    def _validate_phone(self, phone):
        """
        Validate phone number.
        Allows: digits, hyphens, and plus sign at beginning.
        Examples: "+256-701-234567", "0772-123456", "1234567890"
        """
        # Pattern: optional +, then digits and hyphens
        pattern = r'^\+?[\d\-]+$'
        if re.match(pattern, phone):
            return True
        return False
    
    def _validate_email(self, email):
        """
        Validate email address.
        Must contain '@' and at least one '.' after the '@'.
        """
        if email == "":  # Email is optional
            return True
        
        # Check for @ symbol
        if '@' not in email:
            return False
        
        # Check for at least one dot after @
        parts = email.split('@')
        if len(parts) != 2:
            return False
        
        # Check if there's a dot in the domain part
        if '.' not in parts[1]:
            return False
        
        return True
    
    # ============================================================
    # CRUD OPERATIONS
    # ============================================================
    
    def add_contact(self, name, phone, email=""):
        """
        Add a new contact with validation.
         Phone and Email validation.
        """
        # Validate phone number
        if not self._validate_phone(phone):
            print(f"❌ Error: Invalid phone number '{phone}'.")
            print("   Phone numbers can only contain digits, hyphens, and a leading '+'.")
            return False
        
        # Validate email
        if not self._validate_email(email):
            print(f"❌ Error: Invalid email '{email}'.")
            print("   Email must contain '@' and at least one '.' after it.")
            return False
        
        # Check if contact already exists
        for contact in self.contacts:
            if contact['name'].lower() == name.lower():
                print(f"❌ Error: Contact '{name}' already exists.")
                return False
        
        # Add contact
        contact = {
            'name': name,
            'phone': phone,
            'email': email
        }
        self.contacts.append(contact)
        print(f"✅ Contact '{name}' added successfully!")
        return True
    
    def view_contact(self, name):
        """
        View a single contact by name.
        """
        for contact in self.contacts:
            if contact['name'].lower() == name.lower():
                self._display_contacts([contact])
                return True
        
        print(f"❌ Contact '{name}' not found.")
        return False
    
    def update_contact(self, name, new_phone=None, new_email=None):
        """
        Update an existing contact's phone and/or email.
         Validation applied to new values.
        """
        for contact in self.contacts:
            if contact['name'].lower() == name.lower():
                # Validate new phone if provided
                if new_phone is not None:
                    if not self._validate_phone(new_phone):
                        print(f"❌ Error: Invalid phone number '{new_phone}'.")
                        return False
                    contact['phone'] = new_phone
                    print(f"✅ Phone updated to '{new_phone}'")
                
                # Validate new email if provided
                if new_email is not None:
                    if not self._validate_email(new_email):
                        print(f"❌ Error: Invalid email '{new_email}'.")
                        return False
                    contact['email'] = new_email
                    print(f"✅ Email updated to '{new_email}'")
                
                print(f"✅ Contact '{name}' updated successfully!")
                return True
        
        print(f"❌ Contact '{name}' not found.")
        return False
    
    def delete_contact(self, name):
        """
        Delete a contact by name.
        """
        for i, contact in enumerate(self.contacts):
            if contact['name'].lower() == name.lower():
                deleted = self.contacts.pop(i)
                print(f"✅ Contact '{deleted['name']}' deleted successfully!")
                return True
        
        print(f"❌ Contact '{name}' not found.")
        return False
    
    # ============================================================
    #  ADVANCED SEARCH
    # ============================================================
    
    def search_contacts(self, search_term):
        """
        Search for contacts by name, phone, or email.
        Added email search capability.
        """
        if not self.contacts:
            print("📋 No contacts available to search.")
            return []
        
        results = []
        search_term_lower = search_term.lower()
        
        for contact in self.contacts:
            # Search by name
            if search_term_lower in contact['name'].lower():
                results.append(contact)
            # Search by phone
            elif search_term_lower in contact['phone'].lower():
                results.append(contact)
            # Search by email 
            elif search_term_lower in contact['email'].lower():
                results.append(contact)
        
        # Display results in clean format
        if results:
            print(f"\n✅ Found {len(results)} contact(s):")
            self._display_contacts(results)
        else:
            print(f"❌ No contacts found matching '{search_term}'.")
        
        return results
    
    def list_all_contacts(self):
        """
        Display all contacts in a clean format.
        """
        if not self.contacts:
            print("📋 No contacts available.")
            return
        
        print(f"\n📋 Total Contacts: {len(self.contacts)}")
        self._display_contacts(self.contacts)
    
    def _display_contacts(self, contacts):
        """
        Helper method to display contacts in a clean, formatted way.
        User-friendly format for search results.
        """
        if not contacts:
            return
        
        # Determine column widths
        max_name = max(len(c['name']) for c in contacts)
        max_phone = max(len(c['phone']) for c in contacts)
        max_email = max(len(c['email']) for c in contacts)
        
        # Set minimum widths
        max_name = max(max_name, 10)
        max_phone = max(max_phone, 10)
        max_email = max(max_email, 10)
        
        # Print header
        print("\n" + "=" * (max_name + max_phone + max_email + 10))
        print(f"{'Name'.ljust(max_name)} | {'Phone'.ljust(max_phone)} | {'Email'.ljust(max_email)}")
        print("-" * (max_name + max_phone + max_email + 10))
        
        # Print contacts
        for contact in contacts:
            name = contact['name'][:max_name].ljust(max_name)
            phone = contact['phone'][:max_phone].ljust(max_phone)
            email = contact['email'][:max_email].ljust(max_email)
            print(f"{name} | {phone} | {email}")
        
        print("=" * (max_name + max_phone + max_email + 10))


# ============================================================
# INTERACTIVE CLI MENU
# ============================================================

def main():
    """
    Interactive CLI Menu for the Contact Management System.
    Full CLI interface with proper input handling.
    """
    manager = ContactManager()
    
    # Sample data to start with
    sample_contacts = [
        ("Kirabo Eria", "+256-701-234567", "eria@example.com"),
        ("John Doe", "0772-123456", "john@example.com"),
        ("Sarah Smith", "+1-555-6789", "sarah@example.com")
    ]
    
    for name, phone, email in sample_contacts:
        manager.add_contact(name, phone, email)
    
    print("\n" + "=" * 50)
    print("   📇 WELCOME TO CONTACT MANAGER")
    print("=" * 50)
    print("Sample contacts loaded. Let's get started!")
    
    while True:
        print("\n" + "=" * 40)
        print("   CONTACT MANAGER MENU")
        print("=" * 40)
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contacts")
        print("6. List All Contacts")
        print("7. Exit")
        print("=" * 40)
        
        choice = input("Choose an option (1-7): ").strip()
        
        # ========== OPTION 1: ADD CONTACT ==========
        if choice == "1":
            print("\n--- ADD NEW CONTACT ---")
            name = input("Enter name: ").strip()
            if not name:
                print("❌ Name cannot be empty.")
                continue
            
            phone = input("Enter phone (e.g., +256-701-234567): ").strip()
            if not phone:
                print("❌ Phone number cannot be empty.")
                continue
            
            email = input("Enter email (optional, press Enter to skip): ").strip()
            
            manager.add_contact(name, phone, email)
        
        # ========== OPTION 2: VIEW CONTACT ==========
        elif choice == "2":
            print("\n--- VIEW CONTACT ---")
            name = input("Enter contact name to view: ").strip()
            if not name:
                print("❌ Name cannot be empty.")
                continue
            manager.view_contact(name)
        
        # ========== OPTION 3: UPDATE CONTACT ==========
        elif choice == "3":
            print("\n--- UPDATE CONTACT ---")
            name = input("Enter contact name to update: ").strip()
            if not name:
                print("❌ Name cannot be empty.")
                continue
            
            # Check if contact exists first
            found = False
            for contact in manager.contacts:
                if contact['name'].lower() == name.lower():
                    found = True
                    break
            
            if not found:
                print(f"❌ Contact '{name}' not found.")
                continue
            
            print("Leave blank to keep current value.")
            new_phone = input(f"New phone (current: {contact['phone']}): ").strip()
            new_email = input(f"New email (current: {contact['email']}): ").strip()
            
            # Only update if new values were provided
            if new_phone == "":
                new_phone = None
            if new_email == "":
                new_email = None
            
            if new_phone is None and new_email is None:
                print("❌ No changes provided.")
                continue
            
            manager.update_contact(name, new_phone, new_email)
        
        # ========== OPTION 4: DELETE CONTACT ==========
        elif choice == "4":
            print("\n--- DELETE CONTACT ---")
            name = input("Enter contact name to delete: ").strip()
            if not name:
                print("❌ Name cannot be empty.")
                continue
            
            # Confirm deletion
            confirm = input(f"Are you sure you want to delete '{name}'? (yes/no): ").strip().lower()
            if confirm == "yes":
                manager.delete_contact(name)
            else:
                print("❌ Deletion cancelled.")
        
        # ========== OPTION 5: SEARCH CONTACTS ==========
        elif choice == "5":
            print("\n--- SEARCH CONTACTS ---")
            print("Search by name, phone, or email.")
            search_term = input("Enter search term: ").strip()
            if not search_term:
                print("❌ Search term cannot be empty.")
                continue
            manager.search_contacts(search_term)
        
        # ========== OPTION 6: LIST ALL CONTACTS ==========
        elif choice == "6":
            print("\n--- ALL CONTACTS ---")
            manager.list_all_contacts()
        
        # ========== OPTION 7: EXIT ==========
        elif choice == "7":
            print("\n👋 Thank you for using Contact Manager!")
            print("   Goodbye!")
            break
        
        # ========== INVALID OPTION ==========
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 7.")


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
