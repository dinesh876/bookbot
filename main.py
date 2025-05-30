import sys
from stats import get_num_words,get_char_count,sort_by_count



if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

FILE_PATH = sys.argv[1]

def main():
    num_words = get_num_words(FILE_PATH)
    char_count = get_char_count(FILE_PATH)
    sorted_dict = sort_by_count(char_count)
    
    print(f"{'='*12} BOOKBOT {'='*12}")
    print("Analyzing book found at books/frankenstein.txt...")
    print(f"{'-'*12} Word Count {'-'*12}")
    print(f"Found {num_words} total words")
    print(f"{'-'*12} Character Count {'-'*12}")  
    
    for key in sorted_dict:
        if key.isalpha():
            print(f'{key}: {sorted_dict[key]}')
    
    print(f"{'='*12} END {'='*12}")
    
if __name__ == "__main__":
    main()