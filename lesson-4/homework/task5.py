
minlength = 8

while True:
    password = input("Enter pasword:\n")
    if len(password) >= minlength:
        if any(char.isupper() for char in password):
            print("Password is strong.")
            break
        else:
            print("Add at least one uppercase.")
    else:
        print("Password is too short")

