import sys
import math
import func

"""Proccess code"""

# list of functions
functioned = {}


def interpret(input):
    if ";define" not in input:
        if ";add" in input:
            name, mth = input.split(" ")
            num1, num2 = mth.split("+")
            num1 = int(num1)
            num2 = int(num2)
            print(num1 + num2)
        elif "//;" in input:
            pass
        elif ";sub" in input:
            name, mth = input.split(" ")
            num1, num2 = mth.split("-")
            num1 = int(num1)
            num2 = int(num2)
            print(num1 - num2)
        elif ";mul" in input:
            name, mth = input.split(" ")
            num1, num2 = mth.split("*")
            num1, num2 = int(num1), int(num2)
            print(num1 * num2)
        elif ";div" in input:
            name, mth = input.split(" ")
            num1, num2 = mth.split("/")
            num1, num2 = int(num1), int(num2)
            print(num1 / num2)
        elif ";pow" in input:
            name, mth = input.split(" ")
            num1, num2 = mth.split("^")
            num1, num2 = int(num1), int(num2)
            print(num1**num2)
        elif ";newline" in input:
            print("\n")
        elif ";printf" in input:
            name, filename = input.split(" ")
            with open(filename) as file:
                for line in file:
                    print(line)
        elif ";root" in input:
            name, mth = input.split(" ")
            mth = int(mth)
            answer = math.sqrt(mth)
            print(answer)
        elif ";write~" in input:
            name, content1 = input.split("~")
            content, filename = content1.split("|filename|")
            with open(filename, "a") as file:
                file.write(content)
        elif ";overwrite~" in input:
            name, content1 = input.split("~")
            content, filename = content1.split("|filename|")
            with open(filename, "w") as file:
                file.write(content)
        elif input.startswith(";") and input[1:] in functioned:
            action = functioned[input[1:]]
            func.proccess(action)
        else:
            print(input)
    elif ";define" in input:
        name, content = input.split("`")
        funcname, action = content.split(">")
        functioned[funcname] = action

    else:
        pass


def openfile(filename):
    with open(filename) as file:
        for line in file:
            interpret(line)


def shell():
    print(
        "Welcome to the interactive shell. The Shell allows you to run commands\nexit() to exit"
    )
    while True:
        shellinput = input(">> ")
        if shellinput == "exit()":
            return
        if shellinput == "sys.exit()":
            sys.exit()



