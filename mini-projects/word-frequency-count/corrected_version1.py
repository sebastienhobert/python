import string


def count_word_frequency(file_path):
    # Remove any extraneous or invisible characters from the file path
    clean_path = file_path.replace('\u202a', '').strip()

    # Create an empty dictionary to store word frequencies
    word_freq = {}

    # Open the file and read its contents
    try:
        with open(clean_path, 'r', encoding='utf-8') as file:
            # Read the file line by line
            for line in file:
                # Remove any punctuation and convert the line to lowercase
                line = line.translate(str.maketrans('', '', string.punctuation)).lower()
                # Split the line into words
                words = line.split()
                # Update the word frequency dictionary
                for word in words:
                    if word in word_freq:
                        word_freq[word] += 1
                    else:
                        word_freq[word] = 1
        return word_freq
    except FileNotFoundError:
        print(f"The file at {clean_path} was not found. Please check the path and try again.")
    except PermissionError:
        print(f"Permission denied for file at {clean_path}. Please check your file permissions and try again.")
    except UnicodeDecodeError as e:
        print(f"An error occurred while decoding the file: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}


if __name__ == "__main__":
    # Input: Get the file path from the user
    file_path = input("Enter the full path to the text file (e.g., C:\\Users\\sebwa\\Downloads\\example.txt): ").strip()

    # Count the word frequencies in the file
    word_freq = count_word_frequency(file_path)

    # Display the word frequencies
    if word_freq:
        print("Word frequencies:")
        for word, freq in word_freq.items():
            print(f"{word}: {freq}")
