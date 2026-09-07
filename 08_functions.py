# ------------------------------------------------
# 1. SIMPLE FUNCTION
# ------------------------------------------------

def greet():
    print("Hello Nithiya Sharwin!")


greet()


# ------------------------------------------------
# 2. FUNCTION WITH A PARAMETER
# ------------------------------------------------

def greet_user(name):
    print(f"Hello {name}!")


greet_user("Sharwin")


# ------------------------------------------------
# 3. FUNCTION WITH TWO PARAMETERS
# ------------------------------------------------

def add_numbers(a, b):
    print("Sum:", a + b)


add_numbers(10, 20)


# ------------------------------------------------
# 4. FUNCTION WITH RETURN
# ------------------------------------------------

def multiply_numbers(a, b):
    return a * b


result = multiply_numbers(5, 4)

print("Multiplication:", result)


# ------------------------------------------------
# 5. FUNCTION FOR AVERAGE
# ------------------------------------------------

def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average


marks = [85, 90, 78, 92, 88]

average = calculate_average(marks)

print("Average Marks:", average)


# ------------------------------------------------
# 6. FUNCTION WITH CONDITION
# ------------------------------------------------

def check_result(marks):

    if marks >= 50:
        return "Pass"
    else:
        return "Fail"


result = check_result(75)

print("Result:", result)


# ------------------------------------------------
# 7. DEFAULT PARAMETER
# ------------------------------------------------

def greet_student(name="Student"):
    print(f"Hello {name}!")


greet_student()
greet_student("Sharwin")


# ------------------------------------------------
# 8. AI/ML STYLE FUNCTION
# ------------------------------------------------

def calculate_accuracy(correct, total):
    accuracy = (correct / total) * 100
    return accuracy


correct_predictions = 92
total_predictions = 100

accuracy = calculate_accuracy(
    correct_predictions,
    total_predictions
)

print("Model Accuracy:", accuracy, "%")