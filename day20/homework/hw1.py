name = input("შეიყვანე შენი სახელი: ")


has_upper = False
for char in name:
    if char.isupper():
        has_upper = True
        break 
if has_upper:
    print(name.lower())
else:
    print(name.capitalize())
