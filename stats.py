def get_num_words(text1):
    word_count = 0
    word_list = text1.split()
    for word in word_list:
        word_count += 1
    return word_count
