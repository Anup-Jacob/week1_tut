#-------------------------------

# Author        : Anup Jacob
# Created date  : 26/09/2021
# Description   : Understanding print function

#-------------------------------

print("\t"*2+"Title")
print("Hello")
print('Hello World')
a = 5
b = 12.3456789
c = a+b
#d = "A number "+b
# Solution - Currently string is added to a float datatype. We need to have same datatype for addition to happen (float + float), (int + int).
e = a+ \
    b+ \
c
f = 2
g = a/f
print(a)
print(b)
print(c)
#print(d)
# Solution - the value d is not used before.
print(e)
print(f)
print(g)