# 1. Create a list with 5 items and output the 2nd item
print("\n--- Question 1 ---")
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
print(f"List: {names}")
print(f"2nd item: {names[1]}")  # Index 1 is 2nd item

# 2. Change the value of the first item to a new value
print("\n--- Question 2 ---")
names[0] = "Amina"
print(f"List after changing first item: {names}")

# 3. Add a sixth item to the list
print("\n--- Question 3 ---")
names.append("Frank")
print(f"List after adding 6th item: {names}")

# 4. Add "Bathel" as the 3rd item
print("\n--- Question 4 ---")
names.insert(2, "Bathel")
print(f"List after inserting 'Bathel' at position 3: {names}")

# 5. Remove the 4th item
print("\n--- Question 5 ---")
removed_item = names.pop(3)  # Index 3 is 4th item
print(f"Removed: {removed_item}")
print(f"List after removing 4th item: {names}")

# 6. Use negative indexing to print the last item
print("\n--- Question 6 ---")
print(f"Last item (negative indexing): {names[-1]}")

# 7. New list with 7 items, print 3rd, 4th, 5th using range
print("\n--- Question 7 ---")
new_list = ["A", "B", "C", "D", "E", "F", "G"]
print(f"New list: {new_list}")
print(f"Items 3-5 (index 2-4): {new_list[2:5]}")

# 8. List of countries and make a copy
print("\n--- Question 8 ---")
countries = ["Uganda", "Kenya", "Tanzania", "Rwanda", "DRC"]
countries_copy = countries.copy()  # or countries[:]
print(f"Original countries: {countries}")
print(f"Copy of countries: {countries_copy}")

# 9. Loop through the list of countries
print("\n--- Question 9 ---")
print("Countries list:")
for country in countries:
    print(f"  - {country}")

# 10. Animal names - sort ascending and descending
print("\n--- Question 10 ---")
animals = ["lion", "elephant", "zebra", "giraffe", "hippo"]
print(f"Original: {animals}")
animals_asc = sorted(animals)
print(f"Ascending: {animals_asc}")
animals_desc = sorted(animals, reverse=True)
print(f"Descending: {animals_desc}")

# 11. Output only animal names with letter 'a'
print("\n--- Question 11 ---")
animals = ["lion", "elephant", "zebra", "giraffe", "hippo", "cat", "dog"]
print(f"All animals: {animals}")
animals_with_a = []
for animal in animals:
    if 'a' in animal:
        animals_with_a.append(animal)
print(f"Animals with 'a': {animals_with_a}")

# 12. Join two lists (first names and second names)
print("\n--- Question 12 ---")
first_names = ["Kirabo", "John", "Sarah"]
last_names = ["Eria", "Doe", "Smith"]
combined_names = first_names + last_names
print(f"First names: {first_names}")
print(f"Last names: {last_names}")
print(f"Combined list: {combined_names}")
