# Given dictionary
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

# 1. Print the value of shoe size
print("\n--- Question 1 ---")
print(f"Shoes dictionary: {Shoes}")
print(f"Shoe size: {Shoes['size']}")

# 2. Change "Nick" to "Adidas"
print("\n--- Question 2 ---")
Shoes["brand"] = "Adidas"
print(f"Updated brand: {Shoes}")

# 3. Add key/value pair "type": "sneakers"
print("\n--- Question 3 ---")
Shoes["type"] = "sneakers"
print(f"Added type: {Shoes}")

# 4. Return list of all keys
print("\n--- Question 4 ---")
print(f"All keys: {Shoes.keys()}")

# 5. Return list of all values
print("\n--- Question 5 ---")
print(f"All values: {Shoes.values()}")

# 6. Check if key "size" exists
print("\n--- Question 6 ---")
if "size" in Shoes:
    print("✅ 'size' key exists in the dictionary")
else:
    print("❌ 'size' key does NOT exist")

# 7. Loop through dictionary
print("\n--- Question 7 ---")
print("Looping through Shoes dictionary:")
for key, value in Shoes.items():
    print(f"  {key}: {value}")

# 8. Remove "color"
print("\n--- Question 8 ---")
del Shoes["color"]
print(f"Dictionary after removing color: {Shoes}")

# 9. Empty the dictionary
print("\n--- Question 9 ---")
Shoes.clear()
print(f"Dictionary after clearing: {Shoes}")

# 10. Dictionary of choice and make a copy
print("\n--- Question 10 ---")
student = {
    "name": "Kirabo Eria",
    "course": "Python Programming",
    "year": 1
}
print(f"Original: {student}")
student_copy = student.copy()
print(f"Copy: {student_copy}")

# 11. Nested dictionaries
print("\n--- Question 11 ---")
students = {
    "student1": {
        "name": "Kirabo",
        "age": 25,
        "course": "Python"
    },
    "student2": {
        "name": "John",
        "age": 22,
        "course": "Java"
    },
    "student3": {
        "name": "Sarah",
        "age": 23,
        "course": "C++"
    }
}
print("Nested dictionary (students):")
for student_id, info in students.items():
    print(f"  {student_id}:")
    for key, value in info.items():
        print(f"    {key}: {value}")

print("\n" + "="*60)
print("ASSIGNMENT COMPLETE!")
print("="*60)