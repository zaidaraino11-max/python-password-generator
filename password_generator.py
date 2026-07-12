import random

class PasswordGenerator:
    def __init__(self):
        self.uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.lowercase = "abcdefghijklmnopqrstuvwxyz"
        self.numbers = "0123456789"
        self.characters = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    def build_pool(self, upper, lower, numbers, characters):
        pool = ""

        if upper.lower() == "y":
            pool += self.uppercase

        if lower.lower() == "y":
            pool += self.lowercase

        if numbers.lower() == "y":
            pool += self.numbers

        if characters.lower() == "y":
            pool += self.characters

        return pool

    def generate_password(self, length, pool):
        password = ""

        for i in range(length):
            password += random.choice(pool)

        return password


def menu():
    print("""
1. GENERATE PASSWORD
0. EXIT
""")


generator = PasswordGenerator()

while True:

    print("\n~~~ PASSWORD GENERATOR ~~~\n")
    menu()

    choice = input("Enter Choice: ")

    if choice == "0":
        print("Goodbye!")
        break

    elif choice != "1":
        print("Invalid choice.")
        continue

    length = int(input("Enter password length: "))

    if length <= 0:
        print("Password length must be greater than 0.")
        continue

    upper = input("Include uppercase letters? (y/n): ")
    lower = input("Include lowercase letters? (y/n): ")
    numbers = input("Include numbers? (y/n): ")
    characters = input("Include special characters? (y/n): ")

    pool = generator.build_pool(upper, lower, numbers, characters)

    if pool == "":
        print("You must select at least one character type.")
        continue

    password = generator.generate_password(length, pool)

    print(f"\nGenerated Password: {password}")
