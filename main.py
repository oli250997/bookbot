from stats import get_num_words
from stats import get_char_count
from stats import analyse
import sys
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    file_content = get_book_text(filepath)
    count = get_num_words(file_content)
    dict = get_char_count(file_content)
    list = analyse(dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for i in list:
        if i["name"].isalpha():
            name = i["name"]
            num = i["num"]
            print(f"{name}: {num}")
    print("============= END ===============")
    return

main()