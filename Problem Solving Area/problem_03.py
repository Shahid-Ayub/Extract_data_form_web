# Problem: Take a list form thr user and find out the second largest number from the list
#          but the that should be a uniqe number?

l = input("Enter your numbers: ")

l = [int(x.strip()) for x in l.split(',')]

uniqe_num = list(set(l))

if len(uniqe_num) < 2:
        print("The number are not enogh ot find the second largest number")
else:
        uniqe_num.sort()
        second_largest =  uniqe_num[-2]

print(second_largest)