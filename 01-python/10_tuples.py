# ------------------------------------------------
# 1. CREATE A TUPLE
# ------------------------------------------------

fruits = ("Apple", "Banana", "Mango", "Orange", "Banana")

print("Fruits Tuple:", fruits)

# ------------------------------------------------
# 2. ACCESS TUPLE ITEMS
# ------------------------------------------------

print("\nFirst Fruit:", fruits[0])
print("Second Fruit:", fruits[1])
print("Last Fruit:", fruits[-1])

# ------------------------------------------------
# 3. LOOP THROUGH TUPLE
# ------------------------------------------------

print("\nLooping Through Tuple:")

for fruit in fruits:
    print(fruit)

# ------------------------------------------------
# 4. COUNT DUPLICATES
# ------------------------------------------------

print("\nNumber of Bananas:", fruits.count("Banana"))

# ------------------------------------------------
# 5. FIND INDEX
# ------------------------------------------------

print("Index of Mango:", fruits.index("Mango"))

# ------------------------------------------------
# 6. LENGTH OF TUPLE
# ------------------------------------------------

print("\nNumber of Fruits:", len(fruits))

# ------------------------------------------------
# 7. TUPLE SLICING
# ------------------------------------------------

marks = (85, 90, 78, 92, 88, 95)

print("\nFirst Three Marks:", marks[:3])
print("Last Two Marks:", marks[-2:])
print("Middle Marks:", marks[2:5])

# ------------------------------------------------
# 8. CONVERT TUPLE TO LIST
# ------------------------------------------------

numbers = (10, 20, 30, 40)

numbers_list = list(numbers)

numbers_list.append(50)

numbers = tuple(numbers_list)

print("\nUpdated Tuple:", numbers)

# ------------------------------------------------
# 9. AI/ML STYLE EXAMPLE
# ------------------------------------------------

image_size = (640, 640)

print("\nImage Size:", image_size)
print("Width:", image_size[0])
print("Height:", image_size[1])