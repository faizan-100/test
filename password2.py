
def main():
    password = str(input("Enter your password : "))
    if (len(password)) >= 5:
        password_Strength(password)
        print("Password is valid")
    else:
        print("Password is invalid, it needs to be longer than 5 characters :|")


def password_Strength(password):
    count = 0
    for i in range(len(password)):
        if password[i] in "!£$%^&*()_@'<>,./?\|+=":
           count += 1
        elif password[i] in "1234567890":
            count += 1
        elif password[i].isupper():
            count += 1

    if count == 1:
        print("Password is weak")
    elif count == 2:
        print("Password ok")
    elif count == 3:
        print("Password is strong")
    
main()
