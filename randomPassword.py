import random

charList = ['!', '@', '#', '$', '%', '^', '&']

def main():
    textPassword = input("Enter a word of your choice for your password: ")
    randomNumber = random.randint(1, 5)
    wordLength = textPassword.__len__()
    randomNumber = random.randint(0, wordLength - 1)
    randomSplCharIndex =  random.randint(0, charList.__len__() - 1)
    charStr = charList[randomSplCharIndex]
    newPwd = textPassword[:randomNumber] + charStr + textPassword[randomNumber+1:] 
    print(newPwd)
    
      
main()
