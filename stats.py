def get_num_words(text1):
    word_count = 0
    word_list = text1.split()
    for word in word_list:
        word_count += 1
    return word_count

def get_num_char(text1):
    char_list = set()
    total_count = {}
    file = list(text1.lower())
    for char in file:
        char_list.add(char)
    for ch in char_list:
        count = 0
        for char in file:
            if char == ch:
                count += 1
        total_count[ch] = count
    '''
    for word in word_list:
        for char in word:
            char_list.add(char.lower())
    '''
    return total_count
