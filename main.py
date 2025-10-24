def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def word_count(path_to_file):
    split_words = ()
    word_count = 0
    with open(path_to_file) as f:
        file_contents = f.read()
    split_words = file_contents.split()
    word_count = len(split_words)
    return word_count



def main():
    #frankenstein_text = get_book_text("./books/frankenstein.txt")
    #print(frankenstein_text)

    frankenstein_word_count = word_count("./books/frankenstein.txt")
    print(f"Found {frankenstein_word_count} total words")


main()