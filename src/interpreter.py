import sys
import math
import re
import func

"""Proccess code"""

# list of functions
functioned = {}
# list of variables
var = {}
# work on TDLI error handling


def interpret(input):
    if ";define" not in input and ";var" not in input:
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
            try:
                name, content1 = input.split("~")
                content, filename = content1.split("|filename|")
                with open(filename, "a") as file:
                    file.write(content)
            except Exception as e:
                print(f"tldt: An error occured: {e}")
        elif ";overwrite~" in input:
            try:
                name, content1 = input.split("~")
                content, filename = content1.split("|filename|")
                with open(filename, "w") as file:
                    file.write(content)
            except Exception as e:
                print(f"tldt: An error occured: {e}")
        elif input.startswith(";") and input[1:] in functioned:
            action = functioned[input[1:]]
            try:
                action, action2, action3, action4, action5 = action.split(":")
                func.proccess(action)
                func.proccess(action2)
                func.proccess(action3)
                func.proccess(action4)
                func.proccess(action5)
            except Exception:
                try:
                    action, action2, action3, action4 = action.split(":")
                    func.proccess(action)
                    func.proccess(action2)
                    func.proccess(action3)
                    func.proccess(action4)
                except Exception:
                    try:
                        action, action2, action3 = action.split(":")
                        func.proccess(action)
                        func.proccess(action2)
                        func.proccess(action3)
                    except Exception:
                        try:
                            action, action2 = action.split(":")
                            func.proccess(action)
                            func.proccess(action2)
                        except Exception:
                            func.proccess(action)
        elif ";sqr" in input:
            name, math = line.split(" ")
            math = int(math)
            print(math**2)
        elif "{" in input:
            try:
                sentence, other = input.split("{")
                varstr, sentence2 = other.split("}")
                if varstr.startswith(";") and varstr[:1] in var:
                    print(sentence+func.process(var[varstr[1:]])+sentence2)
            except Exception as e:
                print(f"tldt: An error occured: {e}")

        else:
            print(input)
    elif ";define" in input:
        try:
            name, content = input.split(">")
            funcname, action = content.split("=")
            functioned[funcname] = action
        except Exception as e:
            print(f"tldt: An error occured: {e}")
    elif ";var" in input:
        try:
            name, content = input.split(">")
            varname, value = content.split("=")
            var[varname] = value
        except Exception as e:
            print(f"tldt: An error occured: {e}")

    else:
        pass


def openfile(filename):
    with open(filename) as file:
        for line in file:
            line = line.rstrip("\n")
            interpret(line)


def shell():
    print(
        "Welcome to the interactive shell. The Shell allows you to run commands\nexit() to exit"
    )
    while True:
        shellinput = input(">> ")
        shellinput = shellinput.rstrip("\n")
        if shellinput == "exit()":
            return
        elif shellinput == "sys.exit()":
            sys.exit()
        elif len(shellinput) < 1:
            pass
        else:
            interpret(shellinput)
