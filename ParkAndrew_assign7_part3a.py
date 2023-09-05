import random
import string


#function 1 ascii shift
def asciishift(string1,num):
    new_string=''
    for i in range(len(string1)):
        new_string+=chr(ord(string1[i])+num)
    return new_string
word = "ABCDEFG"
for num in range(-5, 6):
    print( asciishift(word, num))

#function 2 shift right
def shiftright(word):
    return word[len(word)-1:]+word[0 : len(word)-1]

#function 3 shift left
def shiftleft(word):
    return word[1:]+word[0:1]

#function 4 flip
def flip(word):
    word = list(word)
    if len(word)%2==0:
        word[0:len(word)//2],word[len(word)//2:] = word[len(word)//2:],word[0:len(word)//2]
    else:
        word[0:len(word)//2],word[len(word)//2+1:] = word[len(word)//2+1:],word[0:len(word)//2]
    word = "".join(word)
    return word

#function 5 add letters
def add_letters(word,number):
    new_word = ""
    for c in word:
        letters = ""
        for k in range(number): 
            letters += random.choice(string.ascii_letters)   
        new_word += c + letters 
    return new_word

word = "Hello!"
for number in range(1, 5):
    print( add_letters(word,number))

#function 6 delete chs
def delchar(word,x):
    res = ""
    for i in range(0,len(word),1+x):
        res+=word[i]
    return res

word1 = "HdeulHlHom!t"
word2 = "HTLedklFNljioMH!bi"
word3 = "HHHZeZrflqSflz0iosNU!jBk"
word4 = "HFtRKeivFllRNlUlGTaooYwoH!JpXL"
unscrambled1 = delchar(word1,1)
print("Removing 1 character from",word1,"->",unscrambled1)
unscrambled2 = delchar(word2,2)
print("Removing 2 character from",word2,"->",unscrambled2)
unscrambled3 = delchar(word3,3)
print("Removing 3 character from",word3,"->",unscrambled3)
unscrambled4 = delchar(word4,4)
print("Removing 4 character from",word4,"->",unscrambled4)


