# Heber Portal Reyes
# CS 100  2315A 
# HW 06, September 20, 2021


def hasFinalLetter (strList,letters):
    answer = []
    for x in strList:
        if x[-1] in letters:
            answer.append(x)
            answer+=[]
            print (answer[0:])
    return answer

hasFinalLetter (['Car','Taru','Boy','Girl','League','Baki','Sussy Baka', 'JoJo'],'RANDOM')

test1 = hasFinalLetter (['Car','Taru','Boy','Girl','League'],'lOMnYe')
test2 = hasFinalLetter (['Car','Taru','Boy','Girl','League'],'beDru')
test3 = hasFinalLetter (['Car','Taru','Boy','Girl','League','Sussy Baka', 'JoJo'],'MnTW')
print("")

def isDivisible (maxInt,woInts):
    num =[]
    for x in range (1,maxInt):
        if (x % woInts[0] == 0) and (x % woInts[1] == 0):
            num+=[x]
    return num

test1 = isDivisible (100,(3,5))
test2 = isDivisible (50,(5,7))
test3 = isDivisible (15,(7,3))
print(test1)
print(test2)
print(test3)
