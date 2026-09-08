# ------------------------------------------------
# 1. CREATE A SET
# ------------------------------------------------

numbers = {1, 2, 3, 3, 4, 4, 5}

print("Original Set:", numbers)

# ------------------------------------------------
# 2. ADD ELEMENT
# ------------------------------------------------

numbers.add(6)

print("\nAfter add():", numbers)

# ------------------------------------------------
# 3. REMOVE ELEMENT
# ------------------------------------------------

numbers.remove(2)

print("After remove():", numbers)

# ------------------------------------------------
# 4. DISCARD ELEMENT
# ------------------------------------------------

numbers.discard(10)

print("After discard():", numbers)

# ------------------------------------------------
# 5. LENGTH OF SET
# ------------------------------------------------

print("\nLength of Set:", len(numbers))

# ------------------------------------------------
# 6. LOOP THROUGH SET
# ------------------------------------------------

print("\nLooping Through Set:")

for num in numbers:
    print(num)

# ------------------------------------------------
# 7. CHECK ITEM EXISTS
# ------------------------------------------------

print("\nCheck Number:")

if 5 in numbers:
    print("5 is present.")
else:
    print("5 is not present.")

# ------------------------------------------------
# 8. UNION
# ------------------------------------------------

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("\nUnion:", set1.union(set2))

# ------------------------------------------------
# 9. INTERSECTION
# ------------------------------------------------

print("Intersection:", set1.intersection(set2))

# ------------------------------------------------
# 10. DIFFERENCE
# ------------------------------------------------

print("Difference (set1 - set2):", set1.difference(set2))
print("Difference (set2 - set1):", set2.difference(set1))

# ------------------------------------------------
# 11. COPY A SET
# ------------------------------------------------

copy_set = set1.copy()

print("\nCopied Set:", copy_set)

# ------------------------------------------------
# 12. AI/ML STYLE EXAMPLE
# ------------------------------------------------

labels = ["Cat", "Dog", "Dog", "Bird", "Cat", "Horse"]

unique_labels = set(labels)

print("\nOriginal Labels:", labels)
print("Unique Labels:", unique_labels)
print("Number of Unique Classes:", len(unique_labels))