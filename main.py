import sys


def main():
    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    word_list = get_book_text(book_path)
    count = count_words(word_list)
    char_list = count_characters(word_list)
    print("============ BOOKBOT ============")
    print(f"Analazyng book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    sorted_chars = sort_characters(char_list)
    for ch in sorted_chars:
        print(f"{ch['char']}: {ch['num']}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as flapponzo:
        return flapponzo.read()
    
from stats import count_words, count_characters, sort_characters

main()