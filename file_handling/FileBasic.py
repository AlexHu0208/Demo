import os


if __name__ == "__main__":
    # f = open("demofile.txt", "r")
    # print(f.readline())
    # f.close()
    # f = open("demofile2.txt", "a")
    # f.write("Now the file has more content!")
    # f.close()
    # f = open("demofile2.txt", "r")
    # print(f.read())
    # with open("demofile2.txt", "r") as f:
    #     print(f.read())
    # with open("demofile2.txt", "w") as f:
    #     f.write("Replace the content")
    # with open("demofile2.txt", "r") as f:
    #     print(f.read())
    if os.path.exists("demofile.txt"):
        os.remove("demofile.txt")
    else:
        print("The file does not exist")




