# Heber Portal Reyes
# CS 100  2315A 
# HW 10, November 10, 2021
>>> cars = 3

horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']

def initialLetterCount(listOfWords):
    initialDict = {}
    for word in listOfWords:
        if word[0] in  initialDict:
             initialDict[word[0]]= initialDict[word[0]] + 1
        else:
            initialDict[word[0]] = 1
    return initialDict

    
def initialLetters(listOfWords):
    removedDuplicatesHorton = list(dict.fromkeys(listOfWords))
    DictAns = {}
    for word in removedDuplicatesHorton:
        if word[0] in DictAns:
                    DictAns[word[0]].append(word)
        else:
          DictAns[word[0]] = []
          DictAns[word[0]].append(word)
    return DictAns

def shareOneLetter(listOfWords):
    removedDuplicatesHorton = list(dict.fromkeys(listOfWords))
    DictAns = {}
    for word in removedDuplicatesHorton:
        DictAns[word] = []
        DictAns[word].append(word)
        for newword in removedDuplicatesHorton:
             a = list(set(newword)&set(word))
             if len (a)!=0 and (newword not in DictAns[word]):
               DictAns[word].append(newword)
    return DictAns


print(initialLetterCount(horton))
print(initialLetters(horton))
print(shareOneLetter(horton))









































print(initialLetterCount(horton))
