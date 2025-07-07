try:
    name = str(input("Name:"))
    age = int(input("Age:"))
    if age > 18:
        print("allowed")
except :
    if age < 18 :
        print("wait for the next year")