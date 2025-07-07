hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

hours = float(hours)
rate = float(rate)

if hours <= 40:
    pay = hours * rate
else:
    overtime = hours - 40
    pay = (40 * rate) + (overtime * rate * 1.5)

print("Pay:", pay)
