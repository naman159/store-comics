input1 = 0
print("Welcome to your very own Comic DataBase. Your listings are saved in \"comics-list.txt\"! help command can be used to check the features.")

def main():
    f = open("comics-list.txt", "a+")
    global input1
    input1 = input()

    if(input1 == "bye"):
        print("Have a good Day!")
    elif(input1 == "help"):
        print("add: Add a comic or increase the number of chaps read for a certain comic to the list.")
        print("fnd: Find the comic to check the number of chps you have read.")
        print("del: Delete a comic listing.")
        print("lst: List all the comics in your list.")
        print("Example: add abc-1")
    else:
        det = input1[0:3]

        if(det == "add"):
            delete()
            add()
            main()

        elif(det == "fnd"):
            b = find()
            if(b == False):
                print("The comic could not be found in the db!")
            main()

        elif(det == "del"):
            l = delete()
            print(comic1 +" removed!")
            main()

        elif(det == "lst"):
            list()
            main()

        else:
            print("Invalid Command!")
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
            print(istrip('\n'))
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

def list():
    with open("comics-list.txt", "r") as f:
        comics = f.readlines()
    for i in comics:
        print(i.strip('\n'))

main()
