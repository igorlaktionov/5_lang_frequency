import argparse
import re
from collections import Counter


def load_data(filepath):
    try:
        return open(filepath, 'r').read()
    except OSError as error:
        print(error)
        return None


def get_most_frequent_words(words, number_most_popular_words):
    return Counter(words).most_common(number_most_popular_words)


def print_most_frequent_words(most_frequent_words):
    if most_frequent_words and isinstance(most_frequent_words, list):
        for word, qty in most_frequent_words:
            print(word)


def parser_input_data():
    parser = argparse.ArgumentParser()
    parser.add_argument('-filepath', '-f', dest='file_path', required=True, type=str, help='-filepath=/path/to/file')
    parser.add_argument('-number', dest='number_most_popular_words', type=int, default=10)
    return parser.parse_args()


if __name__ == '__main__':
    args = parser_input_data()
    text = load_data(args.file_path)
    if text:
        clear_words = re.findall(r'\w+', text.lower())
        most_frequent_words = get_most_frequent_words(clear_words, args.number_most_popular_words)
        print_most_frequent_words(most_frequent_words)
