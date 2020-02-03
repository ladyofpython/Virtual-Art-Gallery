import random
# print random word from dictionary
def rWord():
    f = open("wordlist.txt", "r")
    txt = f.read()
    # print(txt)
    txt = txt.split('\n')
    # print("lengh txt: "+ str(len(txt)))
    rnum = random.randint(1,len(txt))
    # print("rnum: "+ str(rnum))
    rWord = txt[rnum]
    rWord = rWord.replace("'", "")
    # print("rWord: "+ str(rWord))
    return rWord
