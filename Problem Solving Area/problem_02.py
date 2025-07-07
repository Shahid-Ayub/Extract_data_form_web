# Problem: Write a function that takes two lists and returns a new sorted list 
# containing only the unique elements from both lists.

list_1 = input("Enter Number in your first list: ")
list_2 = input("Enter Number in your Second list: ")

list_1 = [int(x.strip()) for x in list_1.split(',')]
list_2 = [int(x.strip()) for x in list_2.split(',')]

combine_lists =  list_1 + list_2

uniqe_elements = list(set(combine_lists))

uniqe_elements.sort()

print("The unique elements are:", uniqe_elements)
