name = 'Srinivas'
print(name[::-1])
print(type(name))
print(name.upper())
print(list(name))
print(len(name))
print(''.join(reversed(name)))

empty_string = ''
for i in range(len(name)-1,-1,-1):
    empty_string += name[i]

print("Reversed String: ", empty_string)


for i in range(1,10,2):
    print(i*10)
