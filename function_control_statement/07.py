'''
7. Password Strength Checker
Intermediate
Concepts: Conditions, loops, functions, strings
Requirements
•	Accept a password from the user.
•	Check its length.
•	Check for uppercase and lowercase letters.
•	Check for digits and special characters.
•	Classify it as weak, medium, or strong according to your defined rules.
Bonus: Display suggestions to improve a weak password.
'''


def accept_password():
    password = input("Enter your password: ")
    
    score = 0
    upper = False
    lower = False
    digit = False
    special = False
    length = False

    if len(password) < 8:
        score += 0
    elif len(password) > 8 and len(password) < 12:
        score += 1
        length = True
    else:
        score += 2
        length = True

    for ch in password:
        if ch.isupper():
            upper = True
        elif ch.islower():
            lower = True
        elif ch.isdigit():
            digit = True
        else:
            special = True

    if upper:
        score += 1
    if lower:
        score += 1
    if special:
        score += 1
    if digit:
        score += 1

    if score <= 2:
        print("Weak........")
    elif score <= 4:
        print("Medium........")
    else:
        print("Strong Password.......")

    if not length:
        print("Suggestion: Increase the length of your password..........")
    if not upper :
        print("Suggestion: Use uppercase charachters in your password..........")
    if not lower:
        print("Suggestion: Use Lowercase charachters in your password..........")
    if not digit:
        print("Suggestion: Add some digits in your password..........")
    if not special:
        print("Suggestion: Use Special charachters in your password..........")
        
accept_password()