data = open('word.txt'):

def librarian():
    new_lib = {}
    for line in data:
        words = line.strip()
        new_lib.append(word)
    return new_lib

def duplicates(info):
    dictionary = {}
    for words in info:
        dictionary[words] = 1 + dictionary.get(word,0)
        if dictionary[word] > 1:
            return True
        return False

print duplicates()
