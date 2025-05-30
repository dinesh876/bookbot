from collections import defaultdict

def get_num_words(path):
    contents = get_book_text(path)
    return len(contents.split())

def get_char_count(path):
    char_dict = defaultdict()
    for i in get_book_text(path):
        j = i.lower()
        if j not in char_dict:
            char_dict[j] = 0
        char_dict[j] += 1
    
    return char_dict


def sort_by_count(char_dict):
    return dict(sorted(char_dict.items(),key=lambda item:item[1],reverse=True))
    

def get_book_text(path):
    with open(path,'r') as f:
        file_contents = f.read()
    
    return file_contents