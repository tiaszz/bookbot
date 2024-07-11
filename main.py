def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count_word = counting_words(text)
    count_character = counting_characters(text)
    listed_char = chars_dict_to_sorted_list(count_character)

    print(f"--- Begin report of {book_path} ---")
    print(f"{count_word} words found in the document")
    print()

    for item in listed_char:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End Report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def counting_words(text):
    words = text.split()
    count_word = 0
    for word in words:
        count_word += 1
    return count_word

def counting_characters(text):
    chars = {}
    for i in text:
        lowered = i.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

main()

