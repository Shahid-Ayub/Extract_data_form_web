largsest_so_far = -1
print("Before", largsest_so_far)
for the_num in [9, 41, 12, 3,74,15]:
    if the_num > largsest_so_far:
       largsest_so_far = the_num
    print(largsest_so_far, the_num)
       
print("After", largsest_so_far)