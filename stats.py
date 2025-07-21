def get_num_words(content):
    words = content.split()
    total = 0
    for _ in words:
        total += 1
    return total


def get_char_count(content):
    to_lower_content = content.lower()
    char_dict = {}
    for words in to_lower_content:
        for char in words:
            if not char.isalpha():
                continue
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict


def sorted_list_dict(char_dict):
    sorted_list = []
    for char in char_dict:
        sorted_list.append({"char": char, "num": char_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def sort_on(item):
    return item["num"]


def report(num_words, sorted_list, filepath):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_list:
        print(f'{char["char"]}: {char["num"]}')
    print("============= END ===============")
