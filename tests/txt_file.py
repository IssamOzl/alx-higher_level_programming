#!/usr/bin/python3

""" METHODE 1 TO READ FILES """
try:
    f = open("./files/guido_bio.txt")
    txt = f.read()
    f.close()
    #print(txt)
except Exception as e:
    print(e)
    
""" THE EASIEST WAY TO RED FILES """
try:
    with open("./files/guido_bio.txt") as file_obj:
        txt = file_obj.read()
        #print(txt)
except Exception as e:
    print(e)

""" WRITE TO FILE """
lst = ["tst1","tst2","tst3","tst4","tst5"]

with open("./files/write.txt","w") as file_obj:
    for txt in lst:
        print(txt)
        file_obj.write(txt+"\n")
    
