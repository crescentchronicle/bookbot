def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def get_num_words(path_to_file):
    split_words = ()
    word_count = 0
    with open(path_to_file) as f:
        file_contents = f.read()
    split_words = file_contents.split()
    word_count = len(split_words)
    return word_count

def character_count(path_to_file):
    chara_dictionary: dict[str, int] = {}
    with open(path_to_file) as f:
        file_contents = f.read()
    file_contents = file_contents.lower()
    file_contents = list(file_contents)
    for chara in file_contents:
        if chara not in chara_dictionary:
            chara_dictionary[chara] = 1
        else:
            chara_dictionary[chara] += 1
    return chara_dictionary