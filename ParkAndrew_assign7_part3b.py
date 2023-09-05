import string
import random

def validate(ch):
    return ch.upper()=='A' or ch.upper()=='X' or ch.upper()=='F' or ch.upper()=='U' or ch.upper()=='D' or ch.upper()=='L' or ch.upper()=='R'

def add_letters(word):
    i=0
    new_word=''
    while i<len(word):
        new_word+=word[i]+random.choice(string.ascii_letters)
        i+=1
    return new_word

def delChar(word):
    i=0
    new_word=''
    while i<len(word):
        new_word+=word[i]
        i+=2
    return new_word

def flip(word):
    half=int(len(word)/2)
    new_word=''
    for i in range(half,len(word)):
        new_word+=word[i]
    for i in range(half):
        new_word+=word[i]
    return new_word

def asciiIncrement(word):
    new_word=''
    for i in range(len(word)):
        new_word+=chr(ord(word[i])+1)
    return new_word

def asciiDecrement(word):
    new_word=''
    for i in range(len(word)):
        new_word+=chr(ord(word[i])-1)
    return new_word

def shiftleft(word):
    return word[1:]+word[0:1]

def shiftright(word):
    return word[len(word)-1:]+word[0 : len(word)-1]

def main():
   
    pattern=input("Enter an encoder pattern, 'end' to end: ")
  
    while pattern.upper()!="END":
 
        word=input("Enter a word to encode/decode: ")
 
        for i in range(len(pattern)):
            if(validate(pattern[i])):
                if pattern[i].upper()=='A':
                    word=add_letters(word)
                    print('Added 1 character: ',word)
                elif pattern[i].upper()=='F':
                    word=flip(word)
                    print("Flipped: ",word)
                elif pattern[i].upper()=='U':
                    word=asciiIncrement(word)
                    print('ASCII shifted up: ',word)
                elif pattern[i].upper()=='D':
                    word=asciiDecrement(word)
                    print('ASCII shifted down: ',word)
                elif pattern[i].upper()=='L':
                    word=shiftleft(word)
                    print('Shifted left: ',word)
                elif pattern[i].upper()=='R':
                    word=shiftright(word)
                    print('Shifted right: ',word)
                elif pattern[i].upper()=='X':
                    word=delChar(word)
                    print('Deleted 1 character: ',word)
        
        pattern=input("Enter an encoder pattern, 'end' to end: ")

#__name variable = main variable
if __name__=="__main__":
    main()

