import random

def menu():
    print("""1. GENERATE PASSWORD
0. EXIT""")

def password_generator(length, pool):
    password = ""

    for i in range(length):
        password += random.choice(pool)

    return password
    
while True:

    print("\n~~~PASSWORD GENERATOR~~~\n")
    menu()
    choice = input("Enter Choice: ")
    if choice == "0":
        print("Goodbye!")
        break
    if choice != "1":
        print("invalid choice.")
        continue

    UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
    NUMBERS = "0123456789"
    CHARACTERS = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    length = int(input("enter password length: "))

    if length <= 0:
        print("password length must be greater than 0.")
        continue

    pool = ""

    upper = input("include uppercase letters? (y/n): ")
    if upper.lower() == "y":
        pool += UPPERCASE

    lower = input("include lowercase letters? (y/n):")
    if lower.lower() == "y":
        pool += LOWERCASE

    numbers = input("include numbers? (y/n): ")
    if numbers.lower() == "y":
        pool += NUMBERS

    characters = input("include special characters? (y/n): ")
    if characters.lower() == "y":
        pool += CHARACTERS

    if pool == "":
        print("you must select at least one character type.")
        continue

    password = password_generator(length, pool)

    print(f"Generated Password: {password}")

    again = input("generate another password? (y/n): ")
    if again.lower() == "n":
        print("Goodbye!")
        break