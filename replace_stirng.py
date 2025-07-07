name = 'shahid'
re = name.replace('shahid','Ayub') # replace the names or letters what you want.
print(re)   # copy of the name

re2 = name.replace('s','S')
print(re2)   # copy of the name

print(name) # copy the original one

greet = '   Hello   '
ws = greet.lstrip()
print(ws) # skip only left white spaces

ws2 = greet.rstrip()
print(ws2) # skip only right white spaces

ws3 = greet.strip()
print(ws3) # skip both left and right white spaces