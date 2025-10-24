from stats import get_num_words
from stats import character_count

def main():
    #frankenstein_text = get_book_text("./books/frankenstein.txt")
    #print(frankenstein_text)

    frankenstein_word_count = get_num_words("./books/frankenstein.txt")
    print(f"Found {frankenstein_word_count} total words")

    frankenstein_chara_count = character_count("./books/frankenstein.txt")
    print(frankenstein_chara_count)



main()