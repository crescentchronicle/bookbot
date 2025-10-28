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

def sort_on(items):
    return items["num"]

def sort_counts(path_to_file):
    #create function-level variables
    chara_counts_list = []
    chara_counts_dict: dict[str, int] = {}
    #open file and change to string
    with open(path_to_file) as f:
        file_contents = f.read()
    #change string to list of separated characters
    file_contents = file_contents.lower()
    file_contents = list(file_contents)
    #make a loop to parse through characters and adds to chara_counts_dict
    for chara in file_contents:
        if chara not in chara_counts_dict:
            chara_counts_dict[chara] = 1
        else:
            chara_counts_dict[chara] += 1
    #make loop that reads chara_counts_dict and splits key and value pairs into more granular, 
    # smaller dictionaries, with two keys: "name" and "num"
    chara_counts_dict_keys = list(chara_counts_dict.keys())
    for i in range (0, len(chara_counts_dict_keys)):
        chara_data = {}
        chara_data.clear()
        chara_data["name"] = chara_counts_dict_keys[i]
        chara_data["num"] = chara_counts_dict[chara_counts_dict_keys[i]]
        #add smaller dictionaries to chara_counts list
        chara_counts_list.append(chara_data)
    #sort list of dictionaries from greatest to least
    chara_counts_list.sort(reverse=True, key=sort_on)
    return chara_counts_list