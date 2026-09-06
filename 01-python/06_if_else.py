marks = 82

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


 #Python stops after the first True condition.
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry Allowed")
    else:
        print("ID Required")
else:
    print("Under Age")