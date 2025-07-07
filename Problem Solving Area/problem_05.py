# Problem: Take a string from the user and then revrse the string in words not the 
#          whole letters?

text = input("Enter your String: ")

word = text.split()

count = {}

reversed_text = word[::-1]

merg_text = " ".join(reversed_text)

print(merg_text)