import sys
from stats import get_num_words, get_num_char, get_report

def main():
    x = len(sys.argv)
    if x != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    words = get_num_words(text)
    char = get_num_char(text)
    get_report(book_path,words,char)
        

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
