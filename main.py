import sys
from stats import get_num_words, get_char_count, sorted_list_dict, report


def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
        return content


def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    content = get_book_text(filepath)
    num_words = get_num_words(content)
    char_count = get_char_count(content)
    sorted_char_list = sorted_list_dict(char_count)
    report(num_words, sorted_char_list, filepath)


main()
