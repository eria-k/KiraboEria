"""
STUDENT RECORD MANAGEMENT SYSTEM
================================
A menu-driven application that manages student records using CSV and JSON files.
Demonstrates: File I/O, Exception Handling, Logging, Custom Exceptions.
"""

import csv
import json
import os
import logging
from datetime import datetime
import re

# ============================================================
# LOGGING CONFIGURATION
# ============================================================

# Configure logging to write to a file
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('student_system.log'),
        logging.StreamHandler()  # Also print to console
    ]
)

# ============================================================
# CUSTOM EXCEPTIONS
# ============================================================

class StudentNotFoundError(Exception):
    """Raised when a student is not found."""
    pass

class InvalidStudentDataError(Exception):
    """Raised when student data is invalid."""
    pass

class DuplicateStudentError(Exception):
    """Raised when a student with same registration number exists."""
    pass

# ============================================================
# FILE PATHS
# ============================================================

CSV_FILE = 'students.csv'
JSON_FILE = 'students_details.json'

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def initialize_files():
    """Create CSV and JSON files if they don't exist."""
    
    # Create CSV file with headers if it doesn't exist
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['reg_number', 'name', 'program', 'year'])
        logging.info(f"Created {CSV_FILE}")

    # Create JSON file if it doesn't exist
    if not os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'w') as f:
            json.dump({}, f, indent=4)
        logging.info(f"Created {JSON_FILE}")


def load_students():
    """
    Load all students from CSV file.
    Returns a list of dictionaries.
    """
    students = []
    try:
        with open(CSV_FILE, 'r') as f:
            reader = csv.DictReader(f)
            students = list(reader)
        return students
    except FileNotFoundError:
        logging.error(f"{CSV_FILE} not found. Creating new file.")
        initialize_files()
        return []
    except Exception as e:
        logging.error(f"Error loading students: {e}")
        return []


def save_students(students):
    """
    Save students list to CSV file.
    """
    try:
        with open(CSV_FILE, 'w', newline='') as f:
            if students:
                writer = csv.DictWriter(f, fieldnames=students[0].keys())
                writer.writeheader()
                writer.writerows(students)
            else:
                # Write just the headers if empty
                writer = csv.DictWriter(f, fieldnames=['reg_number', 'name', 'program', 'year'])
                writer.writeheader()
        return True
    except Exception as e:
        logging.error(f"Error saving students: {e}")
        return False


def load_json_details():
    """
    Load additional student details from JSON file.
    Returns a dictionary with reg_number as key.
    """
    try:
        with open(JSON_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logging.error(f"{JSON_FILE} not found.")
        return {}
    except json.JSONDecodeError:
        logging.error(f"Error decoding {JSON_FILE}. File may be corrupted.")
        return {}
    except Exception as e:
        logging.error(f"Error loading JSON: {e}")
        return {}


def save_json_details(details):
    """
    Save additional details to JSON file.
    """
    try:
        with open(JSON_FILE, 'w') as f:
            json.dump(details, f, indent=4)
        return True
    except Exception as e:
        logging.error(f"Error saving JSON: {e}")
        return False


def validate_reg_number(reg_number):
    """
    Validate registration number format.
    Format: MUST be 10 characters, e.g., S123456789
    """
    if len(reg_number) != 10:
        raise InvalidStudentDataError("Registration number must be exactly 10 characters")
    if not re.match(r'^S\d{9}$', reg_number):
        raise InvalidStudentDataError("Registration number must start with 'S' followed by 9 digits")
    return True


def validate_name(name):
    """
    Validate name (must not be empty, only letters and spaces).
    """
    if not name or len(name.strip()) == 0:
        raise InvalidStudentDataError("Name cannot be empty")
    if not re.match(r'^[A-Za-z\s]+$', name):
        raise InvalidStudentDataError("Name can only contain letters and spaces")
    return True


def validate_program(program):
    """
    Validate program (must not be empty).
    """
    if not program or len(program.strip()) == 0:
        raise InvalidStudentDataError("Program cannot be empty")
    return True


def validate_year(year):
    """
    Validate year (must be 1-4).
    """
    try:
        year_int = int(year)
        if 1 <= year_int <= 4:
            return True
        else:
            raise InvalidStudentDataError("Year must be between 1 and 4")
    except ValueError:
        raise InvalidStudentDataError("Year must be a number")


def validate_email(email):
    """
    Validate email format.
    """
    if email and not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        raise InvalidStudentDataError("Invalid email format")
    return True


def validate_phone(phone):
    """
    Validate phone number (only digits).
    """
    if phone and not re.match(r'^\+?[\d\-]+$', phone):
        raise InvalidStudentDataError("Phone number should contain only digits and hyphens")
    return True


def find_student_by_reg(reg_number):
    """
    Find a student by registration number.
    Returns student dict if found, raises StudentNotFoundError if not.
    """
    students = load_students()
    for student in students:
        if student['reg_number'] == reg_number:
            return student
    raise StudentNotFoundError(f"Student with registration number {reg_number} not found")


def get_next_reg_number():
    """
    Generate the next registration number.
    Format: S100000001, S100000002, etc.
    """
    students = load_students()
    
    if not students:
        return "S100000001"
    
    # Find the highest registration number
    max_num = 0
    for student in students:
        reg = student['reg_number']
        if reg.startswith('S'):
            try:
                num = int(reg[1:])
                if num > max_num:
                    max_num = num
            except ValueError:
                pass
    
    next_num = max_num + 1
    return f"S{next_num:09d}"  # Format as 9 digits with leading zeros


# ============================================================
# CORE FUNCTIONS
# ============================================================

def add_student():
    """
    Add a new student to the system.
    """
    logging.info("Add student operation started")
    print("\n" + "="*50)
    print("   ADD NEW STUDENT")
    print("="*50)
    
    try:
        # Get basic student details
        print("\n📋 Enter student details:")
        
        # Auto-generate registration number
        reg_number = get_next_reg_number()
        print(f"Registration Number (auto-generated): {reg_number}")
        
        name = input("Student Name: ").strip()
        validate_name(name)
        
        program = input("Program (e.g., Computer Science): ").strip()
        validate_program(program)
        
        year = input("Year (1-4): ").strip()
        validate_year(year)
        
        # Get additional details (JSON data)
        print("\n📋 Enter additional details (press Enter to skip):")
        address = input("Address: ").strip()
        contact = input("Contact Number: ").strip()
        if contact:
            validate_phone(contact)
        email = input("Email: ").strip()
        if email:
            validate_email(email)
        
        # Check for duplicates before saving
        try:
            find_student_by_reg(reg_number)
            raise DuplicateStudentError(f"Student {reg_number} already exists")
        except StudentNotFoundError:
            pass  # This is what we want - student doesn't exist
        
        # Save to CSV
        students = load_students()
        new_student = {
            'reg_number': reg_number,
            'name': name,
            'program': program,
            'year': year
        }
        students.append(new_student)
        
        if not save_students(students):
            raise Exception("Failed to save student data")
        
        # Save additional details to JSON
        details = load_json_details()
        details[reg_number] = {
            'address': address,
            'contact': contact,
            'email': email,
            'date_added': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        save_json_details(details)
        
        print(f"\n✅ Student added successfully!")
        print(f"   Registration Number: {reg_number}")
        logging.info(f"Student added: {reg_number} - {name}")
        
    except InvalidStudentDataError as e:
        print(f"\n❌ Validation Error: {e}")
        logging.warning(f"Validation error: {e}")
    except DuplicateStudentError as e:
        print(f"\n❌ {e}")
        logging.warning(f"Duplicate student: {e}")
    except Exception as e:
        print(f"\n❌ Error adding student: {e}")
        logging.error(f"Error in add_student: {e}")
    finally:
        print("\n" + "-"*50)
        logging.info("Add student operation completed")


def view_all_students():
    """
    Display all students in a formatted table.
    """
    logging.info("View all students operation started")
    print("\n" + "="*70)
    print("   ALL STUDENTS")
    print("="*70)
    
    try:
        students = load_students()
        
        if not students:
            print("\n📋 No students found.")
            logging.info("No students to display")
            return
        
        # Load additional details for formatting
        details = load_json_details()
        
        print(f"\n📋 Total Students: {len(students)}")
        print("-"*70)
        
        # Print header
        print(f"{'Reg Number':<12} {'Name':<20} {'Program':<20} {'Year':<6} {'Contact':<15}")
        print("-"*70)
        
        # Print each student
        for student in students:
            reg = student['reg_number']
            name = student['name'][:20]
            program = student['program'][:20]
            year = student['year']
            
            # Get additional details if available
            contact = details.get(reg, {}).get('contact', '')
            contact = contact[:15] if contact else 'N/A'
            
            print(f"{reg:<12} {name:<20} {program:<20} {year:<6} {contact:<15}")
        
        print("-"*70)
        logging.info(f"Displayed {len(students)} students")
        
    except Exception as e:
        print(f"\n❌ Error viewing students: {e}")
        logging.error(f"Error in view_all_students: {e}")
    finally:
        print("\n" + "="*70)


def view_student_details():
    """
    View detailed information for a specific student.
    """
    logging.info("View student details operation started")
    print("\n" + "="*50)
    print("   VIEW STUDENT DETAILS")
    print("="*50)
    
    try:
        reg_number = input("\nEnter Registration Number: ").strip().upper()
        if not reg_number:
            print("❌ Registration number cannot be empty")
            return
        
        # Find student
        student = find_student_by_reg(reg_number)
        
        # Load additional details
        details = load_json_details()
        extra = details.get(reg_number, {})
        
        # Display student details
        print("\n" + "-"*50)
        print("   STUDENT DETAILS")
        print("-"*50)
        print(f"Registration Number: {student['reg_number']}")
        print(f"Name:               {student['name']}")
        print(f"Program:            {student['program']}")
        print(f"Year:               {student['year']}")
        print(f"Address:            {extra.get('address', 'N/A')}")
        print(f"Contact:            {extra.get('contact', 'N/A')}")
        print(f"Email:              {extra.get('email', 'N/A')}")
        print(f"Date Added:         {extra.get('date_added', 'N/A')}")
        print("-"*50)
        
        logging.info(f"Viewed details for student: {reg_number}")
        
    except StudentNotFoundError as e:
        print(f"\n❌ {e}")
        logging.warning(f"Student not found: {reg_number}")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        logging.error(f"Error in view_student_details: {e}")


def search_students():
    """
    Search for students by name or registration number.
    """
    logging.info("Search students operation started")
    print("\n" + "="*50)
    print("   SEARCH STUDENTS")
    print("="*50)
    
    try:
        search_term = input("\nEnter name or registration number to search: ").strip()
        if not search_term:
            print("❌ Search term cannot be empty")
            return
        
        students = load_students()
        results = []
        search_lower = search_term.lower()
        
        for student in students:
            if (search_lower in student['name'].lower()) or (search_lower in student['reg_number'].lower()):
                results.append(student)
        
        if not results:
            print(f"\n❌ No students found matching '{search_term}'")
            logging.info(f"No results found for: {search_term}")
            return
        
        print(f"\n📋 Found {len(results)} student(s):")
        print("-"*70)
        print(f"{'Reg Number':<12} {'Name':<20} {'Program':<20} {'Year':<6}")
        print("-"*70)
        
        for student in results:
            print(f"{student['reg_number']:<12} {student['name'][:20]:<20} {student['program'][:20]:<20} {student['year']:<6}")
        
        print("-"*70)
        logging.info(f"Search completed. Found {len(results)} results for '{search_term}'")
        
    except Exception as e:
        print(f"\n❌ Error searching: {e}")
        logging.error(f"Error in search_students: {e}")


def update_student():
    """
    Update student details.
    """
    logging.info("Update student operation started")
    print("\n" + "="*50)
    print("   UPDATE STUDENT")
    print("="*50)
    
    try:
        reg_number = input("\nEnter Registration Number to update: ").strip().upper()
        if not reg_number:
            print("❌ Registration number cannot be empty")
            return
        
        # Find the student
        student = find_student_by_reg(reg_number)
        
        print(f"\n📋 Updating student: {student['name']}")
        print("Press Enter to keep current value")
        print("-"*40)
        
        # Update basic details
        new_name = input(f"Name ({student['name']}): ").strip()
        if new_name:
            validate_name(new_name)
            student['name'] = new_name
        
        new_program = input(f"Program ({student['program']}): ").strip()
        if new_program:
            validate_program(new_program)
            student['program'] = new_program
        
        new_year = input(f"Year ({student['year']}): ").strip()
        if new_year:
            validate_year(new_year)
            student['year'] = new_year
        
        # Update JSON details
        details = load_json_details()
        extra = details.get(reg_number, {})
        
        new_address = input(f"Address ({extra.get('address', 'N/A')}): ").strip()
        if new_address:
            extra['address'] = new_address
        
        new_contact = input(f"Contact ({extra.get('contact', 'N/A')}): ").strip()
        if new_contact:
            validate_phone(new_contact)
            extra['contact'] = new_contact
        
        new_email = input(f"Email ({extra.get('email', 'N/A')}): ").strip()
        if new_email:
            validate_email(new_email)
            extra['email'] = new_email
        
        # Save updates
        students = load_students()
        for i, s in enumerate(students):
            if s['reg_number'] == reg_number:
                students[i] = student
                break
        
        if not save_students(students):
            raise Exception("Failed to save student updates")
        
        details[reg_number] = extra
        save_json_details(details)
        
        print(f"\n✅ Student {reg_number} updated successfully!")
        logging.info(f"Student updated: {reg_number}")
        
    except StudentNotFoundError as e:
        print(f"\n❌ {e}")
        logging.warning(f"Student not found: {reg_number}")
    except InvalidStudentDataError as e:
        print(f"\n❌ Validation Error: {e}")
        logging.warning(f"Validation error: {e}")
    except Exception as e:
        print(f"\n❌ Error updating student: {e}")
        logging.error(f"Error in update_student: {e}")


def delete_student():
    """
    Delete a student record.
    """
    logging.info("Delete student operation started")
    print("\n" + "="*50)
    print("   DELETE STUDENT")
    print("="*50)
    
    try:
        reg_number = input("\nEnter Registration Number to delete: ").strip().upper()
        if not reg_number:
            print("❌ Registration number cannot be empty")
            return
        
        # Check if student exists
        student = find_student_by_reg(reg_number)
        
        # Confirm deletion
        print(f"\n⚠️ Are you sure you want to delete:")
        print(f"   Name: {student['name']}")
        print(f"   Registration: {student['reg_number']}")
        confirm = input("\nType 'yes' to confirm: ").strip().lower()
        
        if confirm != 'yes':
            print("❌ Deletion cancelled.")
            logging.info(f"Deletion cancelled for: {reg_number}")
            return
        
        # Remove from CSV
        students = load_students()
        students = [s for s in students if s['reg_number'] != reg_number]
        
        if not save_students(students):
            raise Exception("Failed to delete student from CSV")
        
        # Remove from JSON
        details = load_json_details()
        if reg_number in details:
            del details[reg_number]
            save_json_details(details)
        
        print(f"\n✅ Student {reg_number} deleted successfully!")
        logging.info(f"Student deleted: {reg_number}")
        
    except StudentNotFoundError as e:
        print(f"\n❌ {e}")
        logging.warning(f"Student not found for deletion: {reg_number}")
    except Exception as e:
        print(f"\n❌ Error deleting student: {e}")
        logging.error(f"Error in delete_student: {e}")


# ============================================================
# MENU SYSTEM
# ============================================================

def display_menu():
    """Display the main menu."""
    print("\n" + "="*50)
    print("   STUDENT RECORD MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Add Student")
    print("2. View All Students")
    print("3. View Student Details")
    print("4. Search Students")
    print("5. Update Student")
    print("6. Delete Student")
    print("7. View System Log")
    print("8. Exit")
    print("="*50)


def view_log():
    """Display the last 20 lines of the log file."""
    print("\n" + "="*50)
    print("   SYSTEM LOG (Last 20 entries)")
    print("="*50)
    
    try:
        with open('student_system.log', 'r') as f:
            lines = f.readlines()
            for line in lines[-20:]:
                print(line.strip())
    except FileNotFoundError:
        print("📋 No log file found.")
    except Exception as e:
        print(f"❌ Error reading log: {e}")


def main():
    """Main program loop."""
    
    # Initialize files
    initialize_files()
    
    logging.info("="*50)
    logging.info("STUDENT SYSTEM STARTED")
    logging.info("="*50)
    
    while True:
        try:
            display_menu()
            choice = input("\nEnter your choice (1-8): ").strip()
            
            if choice == '1':
                add_student()
            elif choice == '2':
                view_all_students()
            elif choice == '3':
                view_student_details()
            elif choice == '4':
                search_students()
            elif choice == '5':
                update_student()
            elif choice == '6':
                delete_student()
            elif choice == '7':
                view_log()
            elif choice == '8':
                print("\n👋 Thank you for using the Student Management System!")
                print("   Goodbye!")
                logging.info("SYSTEM EXITED")
                break
            else:
                print("❌ Invalid choice. Please enter 1-8.")
                logging.warning(f"Invalid menu choice: {choice}")
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            logging.info("SYSTEM EXITED (Keyboard Interrupt)")
            break
        except Exception as e:
            print(f"\n❌ An unexpected error occurred: {e}")
            logging.error(f"Unexpected error in main: {e}")


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()