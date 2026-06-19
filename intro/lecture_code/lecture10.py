def makeOrderedList(n):
    myList = []
    for i in range(n + 1):
        myList.append(i)
    return myList


def printList(L):
    for i in L:
        print(i)


def removeElem(L, e):
    newList = []
    for i in L:
        if i != e:
            newList.append(i)
    return newList


def countWords(sentence):
    splitSentence = sentence.split(" ")
    return len(splitSentence)


print(countWords("hello my name is"))
