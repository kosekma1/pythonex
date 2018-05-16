#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Martin
#
# Created:     16/05/2018
# Copyright:   (c) Martin 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Exist two kinds of files: TEXT and BINARY


def fileTest1():
    # print(help(open))

    # simple open and read file
    f = open("guido_bio.txt")
    text = f.read()
    f.close()
    print(text)

def fileTest2():
    # advanced open and read file
    with open("guido_bio.txt") as fobj:    # python automatically close file
        bio = fobj.read()

    print(bio)


def fileTest3():
    # checking existing file
    try:
        with open("guido_bio.txt") as fobj:
            text = fobj.read()
    except FileNotFoundError:
        text = None

    print(text)

def fileTest4():
    # write to file

    oceans = ["Pacific", "Atlantic", "Indian", "Southern", "Arctic"]
    with open("oceans.txt", "w") as f: # "w" switch indicate that we will write to file
        for ocean in oceans:
            f.write(ocean)             # write to file
            f.write("\n")

    with open("oceans.txt", "r") as f:
        text = f.read()
    print(text)

    with open("oceans1.txt", "w") as f:
        for ocean in oceans:
            print(ocean, file=f) # write to file with enters

    with open("oceans1.txt", "r") as f:
        text = f.read()
    print(text)

    with open("oceans1.txt", "a") as f: # appends text to the end of the file

        print(23*"=", file=f)
        print("These are the 5 oceans", file=f)

    with open("oceans1.txt", "r") as f:
        text = f.read()
    print(text)


def main():
    #fileTest1()
    #fileTest2()
    #fileTest3()
    fileTest4()
    pass

if __name__ == '__main__':
    main()
