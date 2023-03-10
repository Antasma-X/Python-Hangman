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
    word=input("enter word:")
    wordList=list(('_' for i in range(len(word))))
    for i in range(len(word)):
        wordListCheck.append(word[i-1])
    

def show():
    print(hangman[numberOfLosses])
    print('Correct Letters:'+str(correctLetters))
    print('Wrong Letters:'+str(wrongLetters))
    print("Number Of Losses:"+str(numberOfLosses))
    print(wordList)

def checkLoss():
    if numberOfLosses==6:
        print('the word was'+word)
        print('You lost!')
        show()
        exit()

def checkWin():
    for i in range(len(word)):
        if wordList[i-1]=='_':
            return
    print('you win')
    show()
    quit()
    
def checkLetter():
    temp=input("Enter Letter:")
    if len(temp)==1 and temp.isalpha :
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

















