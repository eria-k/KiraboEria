first_name=input("Enter your first name: ")
last_name=input("Enter your last name: ")
city=input("Enter your city:")
birth_year=int(input("Enter your birth year: "))
current_year=2026
age=current_year-birth_year
print("\n"+"="*40)
print(f"Hello {first_name} {last_name} from {city}! You are {age} years old.")