import sys
from stats import wordcount
from stats import charcount
from stats import sorted_dict

def get_book_text(path_to_file: str) -> str:
    with open(path_to_file) as f:
        file_contects = f.read()
        return file_contects
    
def main():
    directory = sys.argv[1]
    the_text = (get_book_text(directory))
    numwords = wordcount(the_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {directory}...")
    print("----------- Word Count ----------")
    print(f"Found {numwords} total words")
    print("--------- Character Count -------")
    countlist = (charcount(the_text))
    sortedlist = sorted_dict(countlist)
    for key, value in sortedlist:
        if key.isalpha():
            print(f"{key}: {value}")
    print("============= END ===============")

argv_count = len(sys.argv)
if argv_count != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()
 

