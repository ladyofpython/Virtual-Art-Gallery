import random

f = open("wordlist.txt", "r")
txt = f.read()
# print(txt)

txt = txt.split('\n')

print("lengh txt: "+ str(len(txt)))
rnum = random.randint(1,len(txt))
print("rnum: "+ str(rnum))

rWord = txt[rnum]
print("rWord: "+ str(rWord))

