def get_character_count(book_text: str) -> list:
    char_count = {}
    for word in book_text.lower().split():
        for character in word:
            if character in char_count.keys():
                char_count[character] += 1
            else:
                char_count[character] = 1
    return dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))


def count_words_in_book(book_text: str) -> int:
    num_words = len(book_text.lower().split())
    return num_words
