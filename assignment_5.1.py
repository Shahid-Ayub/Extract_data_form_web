largest = None
smallest = None

while True:
    user_input = input("Enter a number: ")
    if user_input == 'done':
        break
    try:
        num = int(user_input)
    except ValueError:
        print("Invalid input")
        continue

    if largest is None or num > largest:
        largest = num
    if smallest is None or num < smallest:
        smallest = num

print("Maximum is", largest)
print("Minimum is", smallest)
