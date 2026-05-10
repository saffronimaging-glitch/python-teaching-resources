# Simple Login System

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":

    if password == "python123":
        print("Login successful.")

    else:
        print("Incorrect password.")

else:
    print("Username not recognised.")
