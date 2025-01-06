import random
import string  # string module to include uppercase and lowercase letters, digits, and punctuation characters in the password


def generate_password(length):
    # define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    return password


if __name__ == "__main__":
    # input: get user input for the desired password length
    length = int(input("Enter the desired length for the password: "))

    # generate and display the password
    password = generate_password(length)
    print ("Generated password:", password)