print("Exception Handling Demo")

try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Please enter only numbers.")

finally:
    print("Program Finished.")

# AI/ML Example

dataset = [10, 20, "AI", 40]

for value in dataset:
    try:
        print(value / 2)
    except TypeError:
        print("Skipped Non-Numeric Value:", value)