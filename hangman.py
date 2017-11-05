import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    for l in secretWord:
        if l in lettersGuessed:
            return True
        return False

# secretWord = 'apple'
# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(isWordGuessed(secretWord, lettersGuessed))


def getGuessedWord(secretWord, lettersGuessed):
    x = ''
    string = ''
    for l in secretWord:
        if l in lettersGuessed:
            val = l + ' '
        else:
            string = string + x
    return string            

# secretWord = 'apple'
# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(getGuessedWord(secretWord, lettersGuessed))

def getAvailableLetters(lettersGuessed):
    lower = string.ascii_lowercase 
    y = ''
    x = ''
    for l in lower:
        if l not in lettersGuessed:
            y = l
        else:
            y = ''
        x = x + y
    return x

# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(getAvailableLetters(lettersGuessed))


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many 
      letters the secretWord contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.
    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.
    Follows the other limitations detailed in the problem write-up.
    '''
    print ("Professor Lee, I will beat you at Hangman... think of a word", str(len(secretWord)), "length")
    print ('of that length')

    chances = 8
    lettersGuessed=[]
    while guessLeft>0 and not isWordGuessed(secretWord, lettersGuessed):
            print ("You have" + str(chances))
            guess=str.lower(raw_input("Whats the majic letter?: "))
            while len(guess) >0 and guess not in string.ascii_lowercase:
                    guess=str(raw_input("Guess DA letter MAN: "))
            if guess not in lettersGuessed:
                    lettersGuessed.append(guess)
                    if guess in secretWord:
                            print ("VALID GUESS!: ")
                    else:
                            chances= -1
                            print ("HA, WRONGGGGGG:")
            else:
                    print ("Ur low on RAM... You guessed that silly: ")
            print (getGuessedWord(secretWord, lettersGuessed))
    if isWordGuessed(secretWord, lettersGuessed):
            print ("Im Proud of you Prof!")
    else:
            print ("Sorry, YOU TOOK AN L" + str(secretWord))


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)