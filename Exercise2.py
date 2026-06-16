# 1. Output your favorite phone brand
print("\n--- Question 1 ---")
x = ("samsung", "iphone", "tecno", "redmi")
print(f"Phone brands: {x}")
print(f"My favorite brand: {x[1]}")  # iphone

# 2. Negative indexing to print 2nd last item
print("\n--- Question 2 ---")
print(f"2nd last item: {x[-2]}")  # tecno

# 3. Update "iphone" to "itel" (convert to list first)
print("\n--- Question 3 ---")
x_list = list(x)
x_list[1] = "itel"
x = tuple(x_list)
print(f"Updated tuple: {x}")

# 4. Add "Huawei" to tuple (convert to list)
print("\n--- Question 4 ---")
x_list = list(x)
x_list.append("Huawei")
x = tuple(x_list)
print(f"Tuple after adding Huawei: {x}")

# 5. Loop through the tuple
print("\n--- Question 5 ---")
print("Phone brands:")
for brand in x:
    print(f"  - {brand}")

# 6. Remove/delete first item (convert to list)
print("\n--- Question 6 ---")
x_list = list(x)
del x_list[0]
x = tuple(x_list)
print(f"Tuple after removing first item: {x}")

# 7. Tuple of cities in Uganda using tuple() constructor
print("\n--- Question 7 ---")
cities = tuple(["Kampala", "Entebbe", "Jinja", "Gulu", "Mbarara"])
print(f"Cities in Uganda: {cities}")

# 8. Unpack the tuple
print("\n--- Question 8 ---")
city1, city2, city3, city4, city5 = cities
print(f"Unpacked: {city1}, {city2}, {city3}, {city4}, {city5}")

# 9. Range of indexes to print 2nd, 3rd, 4th
print("\n--- Question 9 ---")
print(f"Cities: {cities}")
print(f"2nd-4th cities: {cities[1:4]}")

# 10. Join two tuples
print("\n--- Question 10 ---")
first_names_tuple = ("Kirabo", "John", "Sarah")
last_names_tuple = ("Eria", "Doe", "Smith")
full_names = first_names_tuple + last_names_tuple
print(f"First names tuple: {first_names_tuple}")
print(f"Last names tuple: {last_names_tuple}")
print(f"Joined tuple: {full_names}")

# 11. Tuple of colors multiplied by 3
print("\n--- Question 11 ---")
colors = ("red", "green", "blue")
multiplied_colors = colors * 3
print(f"Original tuple: {colors}")
print(f"Multiplied by 3: {multiplied_colors}")

# 12. Count occurrences of 8
print("\n--- Question 12 ---")
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count_8 = thistuple.count(8)
print(f"Tuple: {thistuple}")
print(f"Number of times 8 appears: {count_8}")
