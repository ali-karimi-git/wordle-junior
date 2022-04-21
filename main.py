from ctypes.wintypes import WORD
from operator import le
from statistics import mean
import sys
from PyDictionary import PyDictionary
import nltk
nltk.download('gutenberg')
from nltk.corpus import gutenberg
import random


moby = set(nltk.Text(gutenberg.words('melville-moby_dick.txt')))
moby = [word.lower() for word in moby if len(word) == 5]

random_word = moby[int(random.random()*len(set(moby)))]

dictionary=PyDictionary()


myword = str(random_word)
print(myword)
yourword = input("guess a word")

meaning = dictionary.meaning(yourword, disable_errors=True)
if meaning is None:
    yourword = input("aslan yani chi? , try another word")

while len(myword) != len(yourword):
    yourword = input("barabar nistan, try another word")


if myword == yourword:
    print ("you did it")
    sys.exit()

myword_list = list(myword)
yourword_list = list(yourword)

print (myword_list)

if len(myword_list) != len(yourword_list):
    print("ham andaze nistan")
    sys.exit()

el = 0
b = 0

guess_list = []

for i in yourword_list:
    if yourword_list[b] == myword_list[el]:
        print("exist " + myword_list[el] + " " ,str(el + 1))
    elif yourword_list[b] != myword_list[el]:
        print("doesnt exist " + yourword_list[b] + " " ,str(el + 1))
        guess_list.append(yourword_list[b])
    b = b + 1
    el = el + 1

for i in yourword_list:
    if i in guess_list:
        print ("hastan vali sare jashoon nistan " +i)
