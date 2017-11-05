
    for char in secretWord:
  if char not in lettersGuessed:
            return False
  return True

Part 2 (value and string have the same indentation)

value = ''
string = ''
    for char in secretWord:
        if char in lettersGuessed:
            value = char + ' '
        else:
            value = "_ " 
        string = string + value        
    return string

Part 3 (import string, lowerstr, vale and str1 all same indentation)

import string
    lowerstr = string.ascii_lowercase
    value = ''
    str1 = ''
    for char in lowerstr:
        if char not in lettersGuessed:
            value = char
        else:
            value = ''    
        str1 = str1 + value
    return str1

Part 4

    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is", str(len(secretWord)), "letters long."
    print "-------------"
    guessLeft=8
    lettersGuessed=[]
    while guessLeft>0 and not isWordGuessed(secretWord, lettersGuessed):
            print "You have",str(guessLeft),"guesses left."
            print "Available letters:",getAvailableLetters(lettersGuessed)
            guess=str(raw_input("Please guess a letter: "))
            guess=guess.lower()
            while len(guess)!=1 and guess not in string.ascii_lowercase:
                    guess=str(raw_input("Please guess a letter: "))
            if guess not in lettersGuessed:
                    lettersGuessed.append(guess)
                    if guess in secretWord:
                            print "Good guess:",
                    else:
                            guessLeft-=1
                            print "Oops! That letter is not in my word:",
            else:
                    print "Oops! You've already guessed that letter:",
            print getGuessedWord(secretWord, lettersGuessed)
            print "------------"
    if isWordGuessed(secretWord, lettersGuessed):
            print "Congratulations, you won!"
    else:
            print "Sorry, you ran out of guesses. The word was", str(secretWord)