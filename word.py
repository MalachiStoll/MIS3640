# fin = open('words.txt')
# line = fin.readline
# print(repr(line))

# fin = open('words.txt')
# for line in fin:
#     word = line.strip()
#     print(word)

"""for words over 20 letters"""
# def long_words():
#     fin = open('words.txt')
#     for line in fin:
#         word = line.strip()
#         if len(word) >20:
#             print(word)
# long_words

# """determine if the word has he letter 'e'"""
# def has_no_e('word'):
#     for letter in word:
#         if letter == 'e':
#             return False

#     return True 

# print (has_no_e('Babson'))

# return not 'e' in word.lower():

# print(has_no_e('Babson'))

# def find_words_no_e():
#     fin = open('wods.txt')
#     counter_no_e = 0
#     counter_total = 0
#     for line in fin:
#         counter_total +=1
#         word = line.strip()
#         if has_no_e(word):
#             #print (word)
#             counter_no_e += 1
#     return counter_no_e/counter_total

# print(find_words_no_e)

# def avoids(word, forbidden):
#     for letter in word:
#          if letter in forbidden:
#              return False
#     return True 



# print(avoides('Babson', 'ab'))
# print(avoides('College', 'ab'))


def find_words_no_vowels():
    fin = open('wods.txt')
    counter_no_e = 0
    counter_total = 0
    for line in fin:
        counter_total +=1
        word = line.strip()
        if has_no_vowels(word,"aeiou"):
            print (word)
            counter_no_vowel += 1
    return counter_no_vowel/counter_total

print(find_words_no_vowels)