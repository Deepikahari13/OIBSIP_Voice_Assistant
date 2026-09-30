import random
import string

while True:
    print("\n--- Random Password Generator---")

    try:
        length = int(input("Enter password length(maximum 8):"))

        if length < 8:
            print("Error:Password length must be at least 8.")
            continue

        print("\nChoose character types:")
        print("1.Uppercase letters")
        print("2.Lowercase letters")
        print("3.Numbers")
        print("4.symbols")

        choices = input("Enter at least 2 choices (example:123):")

        selected = set(choices)

        valid_choices = {"1","2","3","4"}

        if not selected.issubset(valid_choices):
            print("Error:Please choose only 1,2,3, or 4.")
            continue

        if len(selected) < 2:
            print("Error:Select at least 2 character types:")
            continue

        character_pool = ""
        password = []

        if "1" in selected:
            character_pool += string.ascii_uppercase

        password.append(random.choice(string.ascii_uppercase))

        if "2" in selected:
            character_pool += string.ascii_lowercase

        password.append(random.choice(string.ascii_lowercase))

        if "3" in selected:
            character_pool += string.digits

        password.append(random.choice(string.digits))

        if "4" in selected:
            character_pool += string.punctuation

        password.append(random.choice(string.punctuation))

        remaining_length = length - len(password)

        password += [random.choice(character_pool)for _ in range(remaining_length)]

        random.shuffle(password)

        generated_password = "".join(password)

        print("\nGenerated Password:",generated_password)

        again = input("\nGenerate another password? (y/n):").lower()

        if again != "y":
            print("Thank you for using the Password Generator!")
            break

    except ValueError:
        print("Error: Please enter a valid number for password length.")        