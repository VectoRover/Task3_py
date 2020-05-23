import os
path_to_file = "F:/prog/input.txt"
file = open(path_to_file, "r")

try:
    if os.stat(path_to_file).st_size > 0:
        print("file opened successfully")
    if os.stat(path_to_file).st_size == 0:
        print("Error: empty file")
except OSError:
    print("cannot open file")

def possibility(file):
    flag = 0
    string = file.read()
    temp_int = ""
    current1 = ""
    i = 0
    if len(string) == 0:
        print("Error: empty file")
        exit(-3)
    for index in range(len(string)):
        if (string[index] != " ") or (string[index] != "\n"):
            temp_int += string[index]
        if (string[index] == " ") or (string[index] == "\n") or (index == (len(string)) - 1):
            try:
                current2 = int(temp_int)
                if i == 0:
                    current1 = current2
                if (current1 != current2) and ((i == 1) or (index == (len(string)) - 1)):
                    flag += 2
                    current1 = current2
                if current1 != current2:
                    flag += 1
                    current1 = current2
            except ValueError:
                pass
            temp_int = ""
            i += 1
    return flag

def Autotest():
    test_file = open("F:/prog/autotest.txt", "r")
    flag1 = 0
    flag1 = possibility(test_file)
    if flag1 <= 3:
        print("Autotest passed")
    else:
        print("Autotest not passed")
        exit(-1)

Autotest()
flag = possibility(file)
print(flag)
if (flag <= 3):
    print("Possible")
else:
    print("Impossible")





