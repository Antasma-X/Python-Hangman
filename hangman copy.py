
import random
global word
global numberOfLosses
word=''
wordListCheck=[]
numberOfLosses=0
wrongLetters=[]
correctLetters=[]
wordList=[]
hangman=["""
           |-------     
           |      |     
           |
           |
           |
           |
           |
           |
           -------------
           """,
           """
           |-------     
           |      |     
           |      O
           |
           |
           |
           |
           |
           -------------
           """,
           
           """
           |-------     
           |      |     
           |      O
           |      |
           |
           |
           |
           |
           -------------
           """,
            """
           |-------     
           |      |     
           |      O
           |     /|
           |
           |
           |
           |
           -------------
           """,
            """
           |-------     
           |      |     
           |      O
           |     /|\\
           |
           |
           |
           |
           -------------
           """,
            """
           |-------     
           |      |     
           |      O
           |     /|\\
           |     /
           |
           |
           |
           -------------
           """, """
           |-------     
           |      |     
           |      O
           |     /|\\
           |     / \\
           |
           |
           |
           -------------
           """]

def getWord():
    global word
    global wordList
    word=input("enter word:").lower()
    print(word)
    wordList=['_' for i in range(len(word))]
    for i in range(len(word)):
        wordListCheck.append(word[i-1])

def show():
    print(hangman[numberOfLosses])
    print(f'Correct Letters: {correctLetters}')
    print(f'Wrong Letters: {wrongLetters}')
    print(f"Number Of Losses: {numberOfLosses}")
    print(wordList)

def checkLoss():
    if numberOfLosses==6:
        print(f'the word was {word}')
        print('You lost!')
        show()
        exit()

def checkWin():
    for i in range(len(word)):
        if wordList[i-1]=='_':
            return
    show()
    print('you win')
    quit()
    
def checkLetter():
    temp=input("Enter Letter: ").lower()
    if len(temp)==1 and temp.isalpha() and temp not in correctLetters and temp not in wrongLetters :
        x=[pos for pos, char in enumerate(word) if char == temp]
        if x==[]:
            print("Letter not in word")
            global numberOfLosses
            numberOfLosses+=1
            wrongLetters.append(temp)
        
        else:
            print('letter is in word')
            correctLetters.append(temp)
        for i in x:
            wordList[i]=word[i]
    else:
        print("not a letter")
    checkLoss()
    checkWin()
    x=[]


getWord()
while True:
    show()
    checkLetter()

















