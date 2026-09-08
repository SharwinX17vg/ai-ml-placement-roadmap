numbers = [1, 2, 3, 4, 5]

squares = [x * x for x in numbers]
print("Squares:", squares)

even = [x for x in numbers if x % 2 == 0]
print("Even Numbers:", even)

odd = [x for x in numbers if x % 2 != 0]
print("Odd Numbers:", odd)

names = ["Sharwin", "Anu", "Riya"]

upper_names = [name.upper() for name in names]
print("Upper Names:", upper_names)

lengths = [len(name) for name in names]
print("Name Lengths:", lengths)

# AI/ML Example

marks = [85, 90, 78, 92]

normalized = [mark / 100 for mark in marks]

print("Normalized Marks:", normalized)