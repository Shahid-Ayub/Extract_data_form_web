names = {'Shahid, 19','Ahamad. 11','salman, 21'}

user = input("Enter the name: ")
found = False
for name in names:
    if user in name:
        found = True
        print(f"{user} is in the list: {name}")
        break

if not found:
    print(f"{user} is not in the list")
    