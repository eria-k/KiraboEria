
name=input("Enter your name: ")
age=int(input("Enter your age: "))
course=input("Enter your course: ")
student_number=int(input("Enter your student number: "))
def display_info(name, age, course, student_number=None):
    print(f"Name: {name}\nAge: {age}\nCourse: {course}\nStudent Number: {student_number}")

display_info(name, age=age, course=course, student_number=student_number)
    
