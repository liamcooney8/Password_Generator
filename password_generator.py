"""Simple password generator."""


def check_length():
    """Checks that the password length input is valid."""
    while True:
        try:
            pass_length = int(input("\nEnter desired length: "))
            check_encryption(pass_length)
            break
        except ValueError:
            print("\nInvalid. Please try again")


def check_encryption(pass_length):
    """Asks the user to choose their level of encryption for their password."""
    while True:
        try:
            pass_encryption = int(input("\nEncryption Levels:"
                                        "\n\tLevel 1: uppercase + lowercase"
                                        "\n\tLevel 2: uppercase + lowercase + numbers"
                                        "\n\tLevel 3: uppercase + lowercase + numbers + special characters\n"
                                        "\nEnter encryption level (1, 2, or 3):  "))
            if pass_encryption == 1 or pass_encryption == 2 or pass_encryption == 3:
                generate_pass(pass_length, pass_encryption)
                break
            else:
                raise ValueError
        except ValueError:
            print("\n***ONLY ENTER 1, 2, OR 3***")


def generate_pass(length, encryption_level):
    """Sets up mix of elements to create password based off of encryption level."""
    import string
    if encryption_level == 1:
        mix = string.ascii_letters
        string_pass(mix, length)
    elif encryption_level == 2:
        mix = string.ascii_letters + string.digits
        string_pass(mix, length)
    elif encryption_level == 3:
        mix = string.ascii_letters + string.digits + string.punctuation
        string_pass(mix, length)


def string_pass(mix, length):
    """Makes and prints the password with the correct encryption level"""
    import random
    try:
        # Using random.choices instead of random.sample allows for repeats of elements
        temp_password = random.choices(mix, k=length)
        password = "".join(temp_password)
        print(f"\n{password}")
    except TypeError:
        print("Uh oh... something went wrong")


def exit_loop():
    while True:
        prompt = input("\nDo you need another password? Type 'yes' or 'no': ")
        if prompt.lower() == 'yes':
            break
        elif prompt.lower() == 'no':
            print("\nThanks for choosing Liam's password generator!")
            print("Come back soon!\n")
            exit()
        elif prompt.lower() != 'yes' or 'no':
            print("\n***Error: please enter ONLY 'yes' or 'no'***")
