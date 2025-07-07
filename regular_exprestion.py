import re

filename = "regex_sum_2246167.txt"  # Use your own unique file
with open(filename, 'r') as file:
    contents = file.read()

# Find all numbers using regular expressions
numbers = re.findall(r'[0-9]+', contents)

# Convert strings to integers and compute the sum
total = sum([int(num) for num in numbers])

# Print the result
print("Sum:", total)
