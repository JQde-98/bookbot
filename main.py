from operator import itemgetter

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = get_word_count(file_contents)
        character_counts = get_character_counts(file_contents)
        edited_character_counts = remove_symbols(character_counts)
        list_of_dicts = get_list_of_dicts(edited_character_counts)
        sorted_list = sort_list(list_of_dicts)
        print(sorted_list)
        print(f"======Begin book report of {f}")
        for i in sorted_list:
            print(f"The letter {i[0]} appears {i[1]} times.")

        
def get_word_count(file_contents):
    word_list = file_contents.split()
    word_count = 0
    for word in word_list:
        word_count += 1
    return word_count

def get_character_counts(file_contents):
    character_list = []
    character_counts = dict()

    #change the entire text to lowercase
    lower_text = file_contents.lower()
    
    #creates a list of seperate words from the text
    split_text = lower_text.split()
    
    #creates a list of individual characters
    for word in split_text:
       var = list(word)
       for character in var:
          character_list.append(character) 

    #runs through the list of characters and counts them    
    for character in character_list:
        if character not in character_counts:
            character_counts.update({character: 1})
        else:
            character_counts[character] += 1
    
    return character_counts

def remove_symbols(character_counts):
    edited_character_counts = dict()
    for key in character_counts:
        if key.isalpha():
            edited_character_counts.update({key: character_counts[key]})
    return edited_character_counts

def get_list_of_dicts(edited_character_counts):
    list_of_dicts = list(edited_character_counts.items())
    return list_of_dicts

def sort_list(list_of_dicts):
    list_of_dicts.sort(reverse=True, key=itemgetter(1))
    return list_of_dicts
    
main()