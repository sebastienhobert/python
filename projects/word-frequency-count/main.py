# WARNING! the script does not work as it cannot read the file due to OSError: [Errno 22] Invalid argument: '\u202aC:\\Users\\sebwa\\Downloads\\test.txt'
# check 'corrected_version1.py.py' for the working version

import string


def count_word_frequency(file_path):
    # create an empty dictionary to store word frequencies
    word_freq = {}

    # open the file and read its contents
    with open(file_path, 'r') as file:

        # read the file line by line
        for line in file:

            # remove any punctuation and convert the line to lowercase 
            line = line.translate(str.maketrans('', '', string.punctuation)).lower()

            # split the line into words
            words = line.split()

            # update the word frequency dictionary
            for word in words:
                if word in word_freq:
                    word_freq[word] += 1
                else:
                    word_freq[word] = 1

    # return the word frequency dictionary
    return word_freq


if __name__ == "__main__":
    import string

    # input: get the file path from the user
    file_path = input("Enter the path to the text file: ")

    # count the word frequencies in the file
    word_freq = count_word_frequency(file_path)

    # display the word frequencies
    print("Word frequencies:")
    for word, freq in word_freq.items():
        print(f"{word}: {freq}")
