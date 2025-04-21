from stats import get_num_words 
from stats import get_num_char

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = get_num_char(text)
    print(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
