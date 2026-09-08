# CLASS

class Student:

    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def display(self):
        print("\nStudent Details")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Department:", self.department)


student1 = Student("Nithiya Sharwin", 22, "IT")
student2 = Student("Anu", 21, "CSE")

student1.display()
student2.display()

# AI/ML Example

class Prediction:

    def __init__(self, image, label, confidence):
        self.image = image
        self.label = label
        self.confidence = confidence

    def show_prediction(self):
        print("\nPrediction Result")
        print("Image:", self.image)
        print("Class:", self.label)
        print("Confidence:", self.confidence)


result = Prediction("belt_image.jpg", "Tear", 0.96)
result.show_prediction()