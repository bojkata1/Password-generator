import random
import pyperclip


# Decimal numbers of the possible symbol in the ASCII table
LOWER_LIMIT = 33
UPPER_LIMIT = 126
# Length of the generated password
PASSWORD_LENGTH = 12


def generate_password(pass_length, lower_limit, upper_limit):

    # Generates random count of each group of symbols (numbers, uppercase and lowercase letters)
    n_uppercase = random.randint(1, int(pass_length / 4))
    n_lowercase = random.randint(1, int(pass_length / 4))
    numbers = random.randint(1, int(pass_length / 4))
    password = ""

    # While loop for password creation
    while True:

        # While loop that ends only when a valid symbol is found
        while True:
            symbol = random.randint(lower_limit, upper_limit)
            is_valid = True

            if symbol in range(65, 91):
                if n_uppercase:
                    n_uppercase -= 1
                else:
                    is_valid = False

            elif symbol in range(97, 123):
                if n_lowercase:
                    n_lowercase -= 1
                else:
                    is_valid = False

            elif symbol in range(48, 58):
                if numbers:
                    numbers -= 1
                else:
                    is_valid = False

            if is_valid:
                break

        password += chr(symbol)

        if len(password) == pass_length:
            return password


def main():
    password = generate_password(PASSWORD_LENGTH, LOWER_LIMIT, UPPER_LIMIT)
    pyperclip.copy(password)
    print(f"Your new password is: {password}")
    print("It is now copied to the clipboard!")


if __name__ == "__main__":
    main()
