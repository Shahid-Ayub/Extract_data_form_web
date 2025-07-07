import re

with open('invoices.txt','w') as f:
    f.write('''hello my name is shahid and today i eran $1000 per hours
            and my father eran about $3000''')

file_name = "invoices.txt"

with open(file_name,'r') as file:
    contents = file.read()

amounts = re.findall(r'\$(\d+)', contents)

amounts = [int(amount) for amount in amounts]

total = sum(amounts)

print(total)