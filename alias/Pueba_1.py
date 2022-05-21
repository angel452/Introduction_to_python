a = [1,2,3]
b = a
print(id(a))
print(id(b))

b[1] = 12
print (a)