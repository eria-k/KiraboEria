class Student:
    university = "MUK"
    college = "COCIS"
    def __init__(self, name, age, course, student_number):
        self.name = name
        self._age = age
        self.course = course
        self.__student_number = student_number

    def display_info(self):
        print(f"Name: {self.name}\nAge: {self._age}\nCourse: {self.course}\nStudent Number: {self.__student_number}")

eria = Student("Eria", 20, "Computer Science", "12345")
eria.display_info()
print(eria.__student_number)  # This will raise an AttributeError because __student_number is private