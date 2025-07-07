num = 12
is_prime = True

for i in range (2, num):
    if num % i == 0:
        is_prime = False
        break
if is_prime:
    print("the given number is a prime",num)
else:
    print("the given number is not a prime",num)