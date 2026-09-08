# WRITE FILE

with open("student.txt", "w") as file:
    file.write("Nithiya Sharwin\n")
    file.write("Department : IT\n")
    file.write("Learning AI/ML\n")

print("File Created Successfully.")

# READ FILE

with open("student.txt", "r") as file:
    content = file.read()

print("\nFile Content")
print(content)

# APPEND FILE

with open("student.txt", "a") as file:
    file.write("Python Completed.\n")

print("New Line Added.")

# READ AGAIN

with open("student.txt", "r") as file:
    print(file.read())