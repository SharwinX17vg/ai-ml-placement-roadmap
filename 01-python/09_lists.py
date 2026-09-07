# ------------------------------------------------
# 1. CREATE A LIST
# ------------------------------------------------

fruits = ["Apple", "Banana", "Mango", "Orange", "Banana"]

print("Fruits List:", fruits)

# ------------------------------------------------
# 2. ACCESS LIST ITEMS
# ------------------------------------------------

print("\nFirst Fruit:", fruits[0])
print("Second Fruit:", fruits[1])
print("Last Fruit:", fruits[-1])

# ------------------------------------------------
# 3. UPDATE LIST ITEM
# ------------------------------------------------

fruits[2] = "Grapes"

print("\nUpdated List:", fruits)

# ------------------------------------------------
# 4. ADD ITEMS
# ------------------------------------------------

fruits.append("Pineapple")
print("\nAfter append():", fruits)

fruits.insert(1, "Kiwi")
print("After insert():", fruits)

# ------------------------------------------------
# 5. REMOVE ITEMS
# ------------------------------------------------

fruits.remove("Banana")
print("\nAfter remove():", fruits)

removed_item = fruits.pop()
print("Removed Item:", removed_item)
print("After pop():", fruits)

# ------------------------------------------------
# 6. LIST LENGTH
# ------------------------------------------------

print("\nNumber of Fruits:", len(fruits))

# ------------------------------------------------
# 7. LOOP THROUGH LIST
# ------------------------------------------------

print("\nLooping Through List:")

for fruit in fruits:
    print(fruit)

# ------------------------------------------------
# 8. CHECK ITEM EXISTS
# ------------------------------------------------

print("\nCheck Item:")

if "Apple" in fruits:
    print("Apple is available.")
else:
    print("Apple is not available.")

# ------------------------------------------------
# 9. SORT LIST
# ------------------------------------------------

numbers = [45, 10, 80, 25, 60]

numbers.sort()

print("\nAscending Order:", numbers)

numbers.sort(reverse=True)

print("Descending Order:", numbers)

# ------------------------------------------------
# 10. LIST SLICING
# ------------------------------------------------

marks = [85, 90, 78, 92, 88, 95]

print("\nFirst Three Marks:", marks[:3])
print("Last Two Marks:", marks[-2:])
print("Middle Marks:", marks[2:5])

# ------------------------------------------------
# 11. AI/ML STYLE EXAMPLE
# ------------------------------------------------

marks = [85, 90, 78, 92, 88]

total = sum(marks)
average = total / len(marks)

print("\nStudent Marks:", marks)
print("Total:", total)
print("Average:", average)
print("Highest:", max(marks))
print("Lowest:", min(marks))