from collections import Counter
import string

def count_word_frequencies(text):
    # remove punctuation and convert text to lowercase
    text = text.translate(str.maketrans("", "", string.punctuation)).lower()

    # split the text into words
    words = text.split()

    # count the frequency of each word
    word_frequencies = Counter(words)
    return word_frequencies

if __name__ == "__main__":
    text = input("Enter text to analyze: ")
    frequencies = count_word_frequencies(text)

    print("\nWord Frequencies: ")
    for word, count in frequencies.items():
        print(f"{word}: {count}")