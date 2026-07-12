# Password Generator (Python OOP)

A simple command-line password generator built with **Python** using **Object-Oriented Programming (OOP)**. The program allows users to generate secure, random passwords by choosing which character types to include.

## Features

* Generate passwords of any length
* Include uppercase letters (A-Z)
* Include lowercase letters (a-z)
* Include numbers (0-9)
* Include special characters (!@#$%^&*...)
* Menu-driven interface
* Input validation
* Built using Python classes and methods (OOP)

## Technologies Used

* Python 3
* `random` module

## Project Structure

* **PasswordGenerator Class**

  * Stores all available character sets.
  * Builds the character pool based on user selections.
  * Generates a random password.

* **Menu System**

  * Displays available options.
  * Handles user input.
  * Calls the appropriate class methods.

## How to Run

1. Make sure Python 3 is installed.
2. Save the program as `password_generator.py`.
3. Open a terminal in the project folder.
4. Run:

```bash
python password_generator.py
```

## Example

```text
~~~ PASSWORD GENERATOR ~~~

1. GENERATE PASSWORD
0. EXIT

Enter Choice: 1
Enter password length: 12
Include uppercase letters? (y/n): y
Include lowercase letters? (y/n): y
Include numbers? (y/n): y
Include special characters? (y/n): y

Generated Password: A#9kLm2@Qx7!
```

## Concepts Demonstrated

* Classes and Objects
* Constructors (`__init__`)
* Instance Attributes
* Methods
* Loops
* Conditional Statements
* Functions
* User Input
* String Manipulation
* Random Password Generation

## Future Improvements

* Ensure at least one character from each selected category appears in every password.
* Allow users to generate multiple passwords at once.
* Add an option to copy the generated password to the clipboard.
* Save generated passwords to a text file.
* Add a password strength indicator.

## Author

**Zaid Ahmed**

Built as a Python practice project to learn Object-Oriented Programming and strengthen problem-solving skills.
