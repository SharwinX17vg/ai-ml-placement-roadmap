# ------------------------------------------------
# 1. FOR LOOP
# ------------------------------------------------

print("1. FOR LOOP")

for i in range(5):
    print(i)


# ------------------------------------------------
# 2. PRINT NUMBERS FROM 1 TO 10
# ------------------------------------------------

print("\n2. NUMBERS FROM 1 TO 10")

for i in range(1, 11):
    print(i)


# ------------------------------------------------
# 3. EVEN NUMBERS
# ------------------------------------------------

print("\n3. EVEN NUMBERS")

for i in range(2, 21, 2):
    print(i)


# ------------------------------------------------
# 4. ODD NUMBERS
# ------------------------------------------------

print("\n4. ODD NUMBERS")

for i in range(1, 20, 2):
    print(i)


# ------------------------------------------------
# 5. LOOP THROUGH A LIST
# ------------------------------------------------

print("\n5. LOOP THROUGH A LIST")

marks = [85, 90, 78, 92, 88]

for mark in marks:
    print(mark)


# ------------------------------------------------
# 6. CALCULATE TOTAL
# ------------------------------------------------

print("\n6. TOTAL OF MARKS")

total = 0

for mark in marks:
    total = total + mark

print("Total Marks:", total)


# ------------------------------------------------
# 7. CALCULATE AVERAGE
# ------------------------------------------------

print("\n7. AVERAGE OF MARKS")

average = total / len(marks)

print("Average Marks:", average)


# ------------------------------------------------
# 8. WHILE LOOP
# ------------------------------------------------

print("\n8. WHILE LOOP")

i = 1

while i <= 5:
    print(i)
    i = i + 1


# ------------------------------------------------
# 9. BREAK
# ------------------------------------------------

print("\n9. BREAK")

for i in range(1, 11):

    if i == 6:
        break

    print(i)


# ------------------------------------------------
# 10. CONTINUE
# ------------------------------------------------

print("\n10. CONTINUE")

for i in range(1, 11):

    if i == 5:
        continue

    print(i)


# ------------------------------------------------
# 11. LOOP WITH IF CONDITION
# ------------------------------------------------

print("\n11. LOOP WITH IF CONDITION")

for mark in marks:

    if mark >= 90:
        print(mark, "Excellent")

    elif mark >= 75:
        print(mark, "Very Good")

    else:
        print(mark, "Needs Improvement")


# ------------------------------------------------
# 12. SIMPLE MULTIPLICATION TABLE
# ------------------------------------------------

print("\n12. MULTIPLICATION TABLE")

number = 5

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


# ------------------------------------------------
# 13. AI/ML STYLE EXAMPLE
# ------------------------------------------------

print("\n13. AI/ML STYLE EXAMPLE")

predictions = [1, 1, 0, 1, 0]
actual = [1, 0, 0, 1, 0]

correct = 0

for i in range(len(predictions)):

    if predictions[i] == actual[i]:
        correct = correct + 1

accuracy = (correct / len(predictions)) * 100

print("Correct Predictions:", correct)
print("Accuracy:", accuracy, "%")