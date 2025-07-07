# Problem: Take a list from the user and find that how many time a number occured and count
#           it and then print it to the user result?

l = input("Enter your list: ")

l = l.split(',')

lis = []

count = {}

for ele in l:
    lis.append(int(ele.strip()))
    if ele in count:
        count[ele] += 1
    else: 
        count[ele] = 1


print("the count is",count,"your list is",lis)

