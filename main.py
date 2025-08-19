import sys

from stats import count_words_in_book, get_character_count


def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        text = f.read()
    if text:
        return text
    return "Book not found"


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    work_count = count_words_in_book(book_text)
    print(f"Found {work_count} total words")
    print("--------- Character Count -------")
    char_count = get_character_count(book_text)
    for character in char_count.keys():
        print(f"{character}: {char_count[character]}")
