from stats import get_num_words
from stats import character_count
from stats import sort_counts

def main():
    #frankenstein_text = get_book_text("./books/frankenstein.txt")
    #print(frankenstein_text)

    frankenstein_word_count = get_num_words("./books/frankenstein.txt")
    print(f"Found {frankenstein_word_count} total words")

    frankenstein_chara_count = sort_counts("./books/frankenstein.txt")
    print(frankenstein_chara_count)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {frankenstein_word_count} total words")
    print("--------- Character Count -------")
    for i in range(0, len(frankenstein_chara_count)):
        if frankenstein_chara_count[i]["name"].isalpha() == True:
            print(f"{frankenstein_chara_count[i]["name"]}: {frankenstein_chara_count[i]["num"]}")
        else:
            continue
    print("============= END ===============")



main()