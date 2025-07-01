import sys
from stats import count_words
from stats import count_characters
from stats import sort_characters

def get_book_text(file_path):
    with open(file_path, "r") as f:
        book_text = f.read()
    return book_text

"""
def main():
    #file_path = "books/frankenstein.txt"
    book_text = get_book_text(file_path)
    #print(book_text)
"""

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    freq = count_characters(book_text)
    sort_output = sort_characters(freq)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_text)} total words")
    print("--------- Character Count -------")
    for char_info in sort_output:
        print(f"{char_info['char']}: {char_info['num']}")  
    print("============= END ===============")


main()


