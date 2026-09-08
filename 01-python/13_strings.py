text = "Nithiya Sharwin"

print("Original String:", text)

print("\nLength:", len(text))
print("Upper:", text.upper())
print("Lower:", text.lower())
print("Title:", text.title())
print("Replace:", text.replace("Sharwin", "Python"))
print("Count of 'a':", text.count("a"))

print("\nFirst Character:", text[0])
print("Last Character:", text[-1])

print("\nSubstring:", text[0:7])

words = "Python AI ML".split()
print("Split:", words)

joined = "-".join(words)
print("Join:", joined)

print("\nCheck Startswith:", text.startswith("Nithiya"))
print("Check Endswith:", text.endswith("Sharwin"))

sentence = "I am learning AI and Machine Learning."

print("\nContains AI:", "AI" in sentence)

print("\nCharacters:")
for ch in text:
    print(ch)

# AI/ML Example

prompt = "Explain Machine Learning"

print("\nPrompt:", prompt)
print("Prompt Length:", len(prompt))