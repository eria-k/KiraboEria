# 1. Set() constructor to create set of 3 beverages
print("\n--- Question 1 ---")
beverages = set(["coffee", "tea", "juice"])
print(f"Beverages: {beverages}")

# 2. Add 2 more items to beverages
print("\n--- Question 2 ---")
beverages.add("soda")
beverages.add("milk")
print(f"Beverages after adding: {beverages}")

# 3. Check if "microwave" is present
print("\n--- Question 3 ---")
mySet = {"oven", "kettle", "microwave", "refrigerator"}
print(f"Set: {mySet}")
if "microwave" in mySet:
    print("✅ 'microwave' is present in the set")
else:
    print("❌ 'microwave' is NOT present")

# 4. Remove "kettle"
print("\n--- Question 4 ---")
mySet.remove("kettle")
print(f"Set after removing 'kettle': {mySet}")

# 5. Loop through the set
print("\n--- Question 5 ---")
print("Items in mySet:")
for item in mySet:
    print(f"  - {item}")

# 6. Set of 4 items + list of 2 items - add list elements to set
print("\n--- Question 6 ---")
my_set = {"apple", "banana", "cherry", "date"}
my_list = ["elderberry", "fig"]
print(f"Original set: {my_set}")
print(f"List to add: {my_list}")
my_set.update(my_list)
print(f"Updated set: {my_set}")

# 7. Join two sets (ages and first names)
print("\n--- Question 7 ---")
ages = {20, 25, 30}
first_names_set = {"Kirabo", "John", "Sarah"}
combined_set = ages.union(first_names_set)  # or ages | first_names_set
print(f"Ages set: {ages}")
print(f"Names set: {first_names_set}")
print(f"Joined set: {combined_set}")
