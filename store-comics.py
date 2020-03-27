input1 = 0

def main():
    f = open("comics-list.txt", "a+")
    global input1
    input1 = input()
    det = input1[0:3]
    comic1 = input1.split(None, 1)[1]

    if(det == "add"):
        add()
        main()

    if(det == "fnd"):
        b = find()
        if(b == False):
            print("The comic could not be found in the db!")
        main()

    if(det == "del"):
        l = delete()
        print(comic1 +" removed!")
        main()

def add():
    b = find()
    f = open("comics-list.txt", "a+")
    if(b == False):
        comic1 = input1.split(None, 1)[1]
        comic2 = comic1.split("-", 1)[0]
        f.write(comic1 + "\n")
        f.close()
        print(comic1 + " stored!")
    else:
        c = delete()
        print(c)
        add()

def find():
    comic1 = input1.split(None, 1)[1]
    b = False
    with open("comics-list.txt") as f:
        comics = f.readlines()
    for i in comics:
        a = i.split("-", 1)[0]
        if(a == comic1):
            print(i)
            b = True
            break
    return b
    '''if(b == False):
        print("The comic could not be found in the db!")'''

def delete():
    comic1 = input1.split(None, 1)[1]
    with open("comics-list.txt", "r") as f:
        comics = f.readlines()
    with open("comics-list.txt", "w") as f:
        for i in comics:
            a = i.split("-", 1)[0]
            if(a != comic1):
                f.write(i)
    return comic1


main()


'''
        with open("comics-list.txt", "r") as f:
            comics = f.readlines()
        for i in range(len(comics)):
            a = comics[i].split("-", 1)[0]
            if(a == comic2):
                comics[i] = comic1
                with open("comics-list.txt", "w") as f:
                    for i in comics:
                        f.writelines(comics)
                    #print("Changes made! " +str(int(comic1.split("-", 1)[1]) - int(i.split("-", 1)[1]) +"chapters of the comic" +comic2 +" were read!")
'''
