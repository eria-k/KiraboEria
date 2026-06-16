# 1. Concatenate integer and string
print("\n--- Question 1 ---")
age = 25
name = "Kirabo"
# Convert integer to string using str()
concatenated = name + " is " + str(age) + " years old"
print(f"Concatenated: {concatenated}")

# 2. Remove spaces from beginning, middle, end
print("\n--- Question 2 ---")
txt = " Hello, Uganda! "
print(f"Original: '{txt}'")
cleaned = txt.strip()
print(f"Stripped: '{cleaned}'")

# 3. Convert to uppercase
print("\n--- Question 3 ---")
print(f"Uppercase: {txt.upper()}")

# 4. Replace 'U' with 'V'
print("\n--- Question 4 ---")
print(f"Replace 'U' with 'V': {txt.replace('U', 'V')}")

# 5. Return range of characters in 2nd, 3rd, 4th position
print("\n--- Question 5 ---")
y = "I am proudly Ugandan"
print(f"Original: '{y}'")
print(f"Characters 2-4 (index 1-3): '{y[1:4]}'")

# 6. Fix error with quotes
print("\n--- Question 6 ---")
# Option 1: Use double quotes outside, single inside
x1 = 'All "Data Scientists" are cool!'
print(f"Option 1: {x1}")

# Option 2: Escape the inner quotes
x2 = "All \"Data Scientists\" are cool!"
print(f"Option 2: {x2}")