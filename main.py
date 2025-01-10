def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = get_word_count(file_contents)
        character_counts = get_character_counts(file_contents)
        print(f"The number of words in this text: {word_count}")
        print("===============================================")     
        print("The character count of this text:")
        print(character_counts)
        
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

    

main()