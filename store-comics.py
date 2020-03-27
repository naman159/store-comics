input1 = 0

def main():
    f = open("comics-list.txt", "a+")
    global input1
    input1 = input()
    det = input1[0:3]
    comic1 = input1.split(None, 1)[1]

    if(det == "add"):
        delete()
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
    f = open("comics-list.txt", "a+")
    comic1 = input1.split(None, 1)[1]
    comic2 = comic1.split("-", 1)[0]
    f.write(comic1 + "\n")
    f.close()
    print(comic1 + " stored!")

def find():
    comic1 = input1.split(None, 1)[1]
    with open("comics-list.txt") as f:
        comics = f.readlines()
    for i in comics:
        a = i.split("-", 1)[0]
        if(a == comic1):
            print(i)
            return True
    return False

def delete():
    comic1 = input1.split(None, 1)[1]
    comic1 = comic1.split("-", 1)[0]
    with open("comics-list.txt", "r") as f:
        comics = f.readlines()
    with open("comics-list.txt", "w") as f:
        for i in comics:
            a = i.split("-", 1)[0]
            if(a != comic1):
                f.write(i)
    return comic1

main()
