

top_icon = "^"
bottom_icon = "v"
left_icon = "<"
right_icon = ">"

print(top_icon*31)

for i in range(1, 5):
    print(left_icon +" "*29 + right_icon)

print(left_icon +" "+ 'Title' +" "*23 + right_icon)
print(left_icon +" "+ "-"*5 + " "*23 + right_icon)
print(left_icon +" "+ 'Option a' +" "*20 + right_icon)
print(left_icon +" "+ 'Option b' +" "*20 + right_icon)

for i in range(1, 4):
    print(left_icon +" "*29 + right_icon)

print(bottom_icon*31)
