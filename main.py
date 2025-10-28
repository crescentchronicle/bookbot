import sys
from stats import get_num_words
from stats import sort_counts

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)     
    
    word_count = get_num_words(sys.argv[1])

    chara_count = sort_counts(sys.argv[1])

    print("============ BOOKBOT ============")
    print("Analyzing book found at BOOK...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in range(0, len(chara_count)):
        if chara_count[i]["name"].isalpha() == True:
            print(f"{chara_count[i]["name"]}: {chara_count[i]["num"]}")
        else:
            continue
    print("============= END ===============")
    #print(sys.argv)



main()