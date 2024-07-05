## Reading and printing the count of the words in a file
def count_words_in_file(filename: str):
    number_of_words = 0
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            number_of_words += len(words)
    return number_of_words

print(count_words_in_file("sample.txt"))