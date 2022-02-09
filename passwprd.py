password = str(input("enter your password:"))
special_characters = "!@#$%^&*()-+?_=,<>/"

for i in range (len(password)):
    if i > 8:
        a = 1
    else:
        a = 0



    if password[i].islower() and password[i].isupper():
        b = 1
    else:
        b = 0

    if any(i in special_characters for i in password):
        c = 1
    else:
        c = 0

d = (a + b + c)
if d > 3:
    print("Password strenght = strong")
else:
    pass
if d == 2:
    print("Password strength = ok")
else:
    pass
if d == 1:
    print("password strength = weak")
else:
    pass

