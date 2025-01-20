def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
#    print(f"{num_words} words found in the document")
#    print(count_character(text))
    char_frequency_dict = count_character(text)
    sorted_counts = sorted(char_frequency_dict.items(), key=lambda item: item[1], reverse=True)

    for char, count in sorted_counts:
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")
    
def count_character(text):
    char_counts = {}
    for char in text:
        char_lower = char.lower()
        if char_lower in char_counts:
            char_counts[char_lower] += 1
        else:
            char_counts[char_lower] = 1
    return char_counts

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()