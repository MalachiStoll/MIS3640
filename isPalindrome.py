def isPalindrome(word):
    for letters in word:
        if len(word) < 2:
            return True
        if word [0] == word [-1] and word[1: -1]:
            return True

print (isPalindrome("anna"))
