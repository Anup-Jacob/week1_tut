#-------------------------------

# Author        : Anup Jacob
# Created date  : 26/09/2021
# Description   : Printing a pattern/ box

#-------------------------------

top_icon = "^"
bottom_icon = "v"
left_icon = "<"
right_icon = ">"

print(top_icon*31)

# for i in range(1, 5):
print(left_icon +" "*29 + right_icon)
print(left_icon +" "*29 + right_icon)
print(left_icon +" "*29 + right_icon)

print(left_icon +" "*12+ 'Title' +" "*12 + right_icon)
print(left_icon +" "*29 + right_icon)
print(left_icon +" "*29 + right_icon)
print(left_icon +" A "+ 'Option a' +" "*18 + right_icon)
print(left_icon +" B "+ 'Option b' +" "*18 + right_icon)
print(left_icon +" C "+ 'Option c' +" "*18 + right_icon)

# for i in range(1, 4):
print(left_icon +" "*29 + right_icon)
print(left_icon +" "*29 + right_icon)

print(bottom_icon*31)
