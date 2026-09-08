numbers = [10, 20, 30, 40, 50, 60, 70]

print("Original:", numbers)

print("\nFirst 3:", numbers[:3])
print("Last 2:", numbers[-2:])
print("Middle:", numbers[2:5])
print("Every Second:", numbers[::2])
print("Reverse:", numbers[::-1])

text = "MachineLearning"

print("\nString Slicing")
print(text[:7])
print(text[7:])
print(text[::-1])

# AI/ML Example

dataset = ["Image1", "Image2", "Image3", "Image4", "Image5"]

train = dataset[:3]
test = dataset[3:]

print("\nTraining Data:", train)
print("Testing Data:", test)