"""
collect user preferrences
- length
- should contain uppercase
- should contain soecail
- should contain digits

get all avialab;e character
randomly pick character up to the length
ensure we have at least one of each character type
ensure length is valid
"""

import random
import string

def generate_password():
    length = int(input("Enter the desired password length: ").strip())
    include_uppercase = input("Include uppercase letter? (yes/No: ").strip().lower()
    include_specail = input("Include uppercase characters? (yes/No: ").strip().lower()
    include_digits = input("Include uppercase digits? (yes/No: ").strip().lower()

    if length < 4:
        print("passwod length must be at lest 4 character.")
        return
    
    lower = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase else ""
    specail = string.punctuation if include_specail else ""
    digits = string.digits if include_digits == "yes" else ""
    all_characters = lower + uppercase + specail + digits 

    required_characters = []
    if include_uppercase == "yes" :
        required_characters.append(random.choice(uppercase))
    if include_specail == "yes":
        required_characters.append(random.choice(specail))
    if include_digits == "yes":
        required_characters.append(random.choice(digits))

    remaining_length = length - len(required_characters)
    password = required_characters

    for _ in range(remaining_length):
        character = random.choice(all_characters)
        password.append(character)

    random.shuffle(password)

    str_password = "".join(password)
    return str_password

password = generate_password()
print(password)