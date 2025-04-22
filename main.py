from stats import get_num_words, get_num_char, get_report

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = get_num_words(text)
    char = get_num_char(text)
    get_report(book_path,words,char)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
