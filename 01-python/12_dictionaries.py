# ------------------------------------------------
# 1. CREATE A DICTIONARY
# ------------------------------------------------

student = {
    "name": "Nithiya Sharwin",
    "age": 22,
    "department": "IT",
    "cgpa": 8.7
}

print("Student Dictionary:", student)

# ------------------------------------------------
# 2. ACCESS VALUES
# ------------------------------------------------

print("\nStudent Name:", student["name"])
print("Department:", student["department"])

# ------------------------------------------------
# 3. UPDATE VALUE
# ------------------------------------------------

student["age"] = 23

print("\nUpdated Age:", student["age"])

# ------------------------------------------------
# 4. ADD NEW KEY-VALUE PAIR
# ------------------------------------------------

student["city"] = "Puducherry"

print("\nAfter Adding City:", student)

# ------------------------------------------------
# 5. REMOVE VALUE
# ------------------------------------------------

student.pop("cgpa")

print("\nAfter Removing CGPA:", student)

# ------------------------------------------------
# 6. DICTIONARY KEYS
# ------------------------------------------------

print("\nKeys:", student.keys())

# ------------------------------------------------
# 7. DICTIONARY VALUES
# ------------------------------------------------

print("Values:", student.values())

# ------------------------------------------------
# 8. KEY AND VALUE PAIRS
# ------------------------------------------------

print("Items:", student.items())

# ------------------------------------------------
# 9. LOOP THROUGH DICTIONARY
# ------------------------------------------------

print("\nLoop Through Dictionary")

for key, value in student.items():
    print(key, ":", value)

# ------------------------------------------------
# 10. CHECK KEY EXISTS
# ------------------------------------------------

print("\nCheck Key")

if "name" in student:
    print("Name key exists.")
else:
    print("Name key not found.")

# ------------------------------------------------
# 11. COPY DICTIONARY
# ------------------------------------------------

student_copy = student.copy()

print("\nCopied Dictionary:", student_copy)

# ------------------------------------------------
# 12. AI/ML STYLE EXAMPLE
# ------------------------------------------------

prediction = {
    "image_name": "belt_image_01.jpg",
    "class": "Tear",
    "confidence": 0.96,
    "status": "Damage Detected"
}

print("\nAI Prediction")
print("Image:", prediction["image_name"])
print("Class:", prediction["class"])
print("Confidence:", prediction["confidence"])
print("Status:", prediction["status"])