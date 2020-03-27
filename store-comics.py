def main():
    f = open("comics-list.txt", "a+")
    input1 = input()

    det = input1[0:3]
    comic1 = input1.split(None, 1)[1]

    if(det == "add"):
        comic2 = comic1.split("-", 1)[0]
        f.write(comic1 + "\n")
        f.close()
        print(comic1 + " stored!")
        main()

    if(det == "fnd"):
        with open("comics-list.txt") as f:
            comics = f.readlines()
        for i in comics:
            a = i.split("-", 1)[0]
            if(a == comic1):
                print(i)
                break
        main()

    if(det == "del"):
        with open("comics-list.txt", "r") as f:
            comics = f.readlines()
        with open("comics-list.txt", "w") as f:
            for i in comics:
                a = i.split("-", 1)[0]
                if(a != comic1):
                    f.write(i)
        main()

if __name__ == "__main__":
    main()
