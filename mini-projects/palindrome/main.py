def is_palindrome(s):
    # remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()

    # check if the string is equal to its reverse
    return s == s[::-1]  # slice notation works as s[start:stop:step]


if __name__ == "__main__":
    # input: get user input for a string
    user_string = input("Enter a string: ")

    # check if the string is a palindrome
    if is_palindrome(user_string):
        print(f'{user_string} is a palindrome.')
    else:
        print(f'{user_string} is not a palindrome.')
