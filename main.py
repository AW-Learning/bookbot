def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words =get_book_word_count(text)
    print(f"{words} words found in the document")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_book_word_count(text1):
    word_count = 0
    word_list = text1.split()
    for word in word_list:
        word_count += 1
    return word_count


main()
