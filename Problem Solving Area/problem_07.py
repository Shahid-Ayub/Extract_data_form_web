
# Problem: Take a list form the user and find the average of that list

L = input("Enter you list: ")

numbers = [float(num) for num in L.split()]

sum_numbers = sum(numbers) 

count_num = len(numbers)

average = sum_numbers / count_num

print("the average of your number is:",average)