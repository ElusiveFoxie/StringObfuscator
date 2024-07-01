import sys
import random

def load_words(file_path):
    with open(file_path, 'r') as file:
        words = [line.strip().capitalize() for line in file.readlines()]
    return words

def generate_random_words(num_words, words):
    selected_words = random.sample(words, num_words)
    return ''.join(selected_words)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python generate.py <number_of_words>")
        sys.exit(1)

    num_words = int(sys.argv[1])
    if num_words <= 0:
        print("Please enter a positive integer.")
        sys.exit(1)

    words = load_words('dictionary.txt')
    if num_words > len(words):
        print("Number of words requested exceeds the number of unique words available.")
        sys.exit(1)

    result = generate_random_words(num_words, words)
    print(result)