from stats import get_word_count, get_letter_count, sort_letter_count
import sys


def get_book_text(book):
    with open(book) as f:
        book_content = f.read()
    return book_content

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    letter_dict = get_letter_count(text)
    print("============ BOOKBOT ============\n" \
    f"Analyzing book found at {path}...")
    print("----------- Word Count ----------\n" \
    f"Found {get_word_count(text)} total words")
    print("--------- Character Count -------")
    for i in sort_letter_count(letter_dict):
        if i["char"].isalpha():
            print(i["char"] + ":", i["num"])
    print("============= END ===============")
main()
