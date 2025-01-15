def count_vowels_and_consonants(text):
    vowels = "aeiouAEIOU"
    num_vowels = 0
    num_consonants = 0

    for char in text:
        if char.isalpha():
            if char in vowels:
                num_vowels += 1
            else:
                num_consonants += 1

    return num_vowels, num_consonants

if __name__ == "__main__":
    text = input("Enter a string: ")
    vowels, consonants = count_vowels_and_consonants(text)
    print(f"Number of vowels: {vowels}")
    print(f"Number of consonants: {consonants}")