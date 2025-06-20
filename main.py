import sys
from stats import get_num_words
from stats import count_chars
from stats import report_characters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    num_words = get_num_words(filepath)
    character_count = report_characters(count_chars(get_book_text(filepath)))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("------- Character Count ---------")

    for c in character_count:
        print(f"{c["char"]}: {c["num"]}")
    
    print("=========== END ============")
main()