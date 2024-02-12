import math
def proccess(input):
    shellinput = input
    if ";add" in shellinput:
        name, mth = shellinput.split(" ")
        num1, num2 = mth.split("+")
        num1 = int(num1)
        num2 = int(num2)
        print(num1 + num2)
    elif "//;" in shellinput:
        pass
    elif ";sub" in shellinput:
        name, mth = shellinput.split(" ")
        num1, num2 = mth.split("-")
        num1 = int(num1)
        num2 = int(num2)
        print(num1 - num2)
    elif ";mul" in shellinput:
        name, mth = shellinput.split(" ")
        num1, num2 = mth.split("*")
        num1, num2 = int(num1), int(num2)
        print(num1 * num2)
    elif ";div" in shellinput:
        name, mth = shellinput.split(" ")
        num1, num2 = mth.split("/")
        num1, num2 = int(num1), int(num2)
        print(num1 / num2)
    elif ";pow" in shellinput:
        name, mth = shellinput.split(" ")
        num1, num2 = mth.split("^")
        num1, num2 = int(num1), int(num2)
        print(num1**num2)
    elif ";newline" in shellinput:
        print("\n")
    elif ";printf" in shellinput:
        name, filename = shellinput.split(" ")
        with open(filename) as file:
            for line in file:
                print(line)
    elif ";root" in shellinput:
        name, mth = shellinput.split(" ")
        mth = int(mth)
        answer = math.sqrt(mth)
        print(answer)
    elif ";write:" in shellinput:
        name, content1 = shellinput.split(":")
        content, filename = content1.split("|filename|")
        with open(filename, "a") as file:
            file.write(content)
    elif ";overwrite:" in shellinput:
        name, content1 = shellinput.split(":")
        content, filename = content1.split("|filename|")
        with open(filename, "w") as file:
            file.write(content)
    else:
        print(shellinput)
 