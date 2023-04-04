# Heber Portal Reyes
# CS 100  2315A 
# HW 08, November 3, 2021

def twoWords(length,firstLetter):
    fWord = "" 
    secWord= ""
    while True:
        fWord = input('A ' + str(length) + '-letter word please. ')
        if length == len(fWord):
            break
        
    while True:
        secWord = input('A word beginning with ' + firstLetter+ ' please: ')
        if secWord[0] == firstLetter.upper() or secWord[0] == firstLetter.lower():
            break
    return [fWord,secWord]
    
print(twoWords(4,'B')) 
 
    
def twoWordsV2(length, firstLetter):
    lst = []
    firstLetter = str(firstLetter).lower()
 
    strlength = "Enter a %s-letter word please:" % (length)
    lettersign = "Enter a word beginning with %s please:" % (firstLetter.upper())
 
    x = input(strlength)
    while len(x) != int(length):
        x = input(strlength)
    else:
        lst.append(x)
 
    y = str(input(lettersign)).lower()
    while y[0] != str(firstLetter):
        y = str(input(lettersign)).lower()
    else:
        lst.append(y)
    return lst
    
print(twoWordsV2(3,'C')) 
def enterNewPassword():

    while True:    
        s = input("Enter password: ")                     
        if 15 < len(s) < 8:
            print("Password must be 8-15 chars long: ")
        elif sum(str.isdigit(c) for c in s) < 1:
            print("Password must contain at least one digit: ") 
        else:
            print("The password is valid. ")
            break
enterNewPassword()


import random 

random_number = random.randint(0,51)
tries = 0
def guessNumber(random_number,tries): 
    
    random_number = random.randint(0,51)
    tries = 0
    print("Guess between 1 & 50")
    guess = int(input("You have a total of 5 Guess : "))
        
    while guess != random_number:
        if guess > random_number:
            print("Guess Lower ")
        if guess < random_number:
            print("Guess Higher ")
            guess = int(input("Try Again : "))
        if guess == random_number:
            print("You are right! I was thinking of ", random_number)
        if tries >= 5: 
            print("You ran out of guesses. The correct number was ", random_number)
            break
        tries += 2        
            
guessNumber(random_number,tries)
