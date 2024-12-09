def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print_report(chars_dict)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    map = {}
    for c in text:
        c = c.lower()
        if c in map.keys():
            map[c] += 1
        else:
            map[c] = 0
    return map

def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(chars_dict):
    if chars_dict is None:
        raise Exception("empty dict")
    for key, val in chars_dict.items():
        print(f"The {key} character was found {val} times")

main()
