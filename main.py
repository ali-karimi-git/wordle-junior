import sys

myword = "ali"
yourword = input()

if myword == yourword:
    print ("you did it")
    sys.exit()

myword_list = list(myword)
yourword_list = list(yourword)

print (myword_list)


el = 0
b = 0

guess_list = []
guess_list2 = []


for i in yourword_list:
    if yourword_list[b] == myword_list[el]:
        print("exist " + myword_list[el] + " " ,str(el + 1))
    elif yourword_list[b] != myword_list[el]:
        guess_list2.append(yourword_list[b])
        #print("doesnt exist " + yourword_list[b] + " " ,str(el + 1))
        guess_list.append(yourword_list[b])
    b = b + 1
    el = el + 1

for i in yourword_list:
    if i in guess_list:
        print ("hastan vali sare jashoon nistan " +i)


