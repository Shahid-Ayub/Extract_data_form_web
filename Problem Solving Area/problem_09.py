# Problem: Ask the user to enter the numbers and then find the sum of the even and ood
#          numbers and then display it?

list_input = input("Enter the numbers: ")
list_input = list_input.split(',')

converted_list_input = [int(x.strip()) for x in list_input]

odd_number = []
even_number = []

for number in converted_list_input:
    if number % 2 != 0:
        odd_number.append(number)
    else:
        even_number.append(number)

sum_of_odd = sum(odd_number)
sum_of_even = sum(even_number)

print("Odd numbers:", odd_number)
print("Even numbers:", even_number)
print("Sum of odd numbers:", sum_of_odd)
print("Sum of even numbers:", sum_of_even)
