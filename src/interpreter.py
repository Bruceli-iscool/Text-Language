import sys
import math
import func

"""Proccess code"""

# list of functions
functioned = {}
# work on TDLI error handling

def interpret(input):
    if ";define" not in input:
        if ";add" in input:
            try:
                name, mth = input.split(" ")
                num1, num2 = mth.split("+")
                num1 = int(num1)
                num2 = int(num2)
                print(num1 + num2)
            except Exception as e:
                print(f"tdt: An error occurred: {e}")
        elif "//;" in input:
            pass
        elif ";sub" in input:
            try:
                name, mth = input.split(" ")
                num1, num2 = mth.split("-")
                num1 = int(num1)
                num2 = int(num2)
                print(num1 - num2)
            except Exception as e:
                print(f"tldt: An error occurred: {e}")
        elif ";mul" in input:
            try:
                name, mth = input.split(" ")
                num1, num2 = mth.split("*")
                num1, num2 = int(num1), int(num2)
                print(num1 * num2)
            except Exception as e:
                print(f"tldt: An error occurred: {e}")
        elif ";div" in input:
            try:
                name, mth = input.split(" ")
                num1, num2 = mth.split("/")
                num1, num2 = int(num1), int(num2)
                print(num1 / num2)
            except Exception as e:
                print(f"tldt: An error occurred: {e}")
        elif ";pow" in input:
            try:
                name, mth = input.split(" ")
                num1, num2 = mth.split("^")
                num1, num2 = int(num1), int(num2)
                print(num1**num2)
            except Exception as e:
                print(f"tldt: An error occurred: {e}")
        elif ";newline" in input:
            print("\n")
        elif ";printf" in input:
            try:
                name, filename = input.split(" ")
                with open(filename) as file:
                    for line in file:
                        print(line)
            except Exception as e:
                print(f"tldt: An error occured: {e}")
        elif ";root" in input:
            try:
                name, mth = input.split(" ")
                mth = int(mth)
                answer = math.sqrt(mth)
                print(answer)
            except Exception as e:
                print(f"tldt: An error occured: {e}")
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
        funcname, action = content.split("=")
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
        elif shellinput == "sys.exit()":
            sys.exit()
        else:
            interpret(shellinput)


