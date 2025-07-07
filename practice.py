names = ['shahid', 'ahmad', 'salman', 'hilal', 'abbas']
user = input(">>> ")
for name in names:
    if user == names:
        names[name] += 1
        print(name)
        continue
    else:
        user == 'done'
        break

print("we are done bro")
