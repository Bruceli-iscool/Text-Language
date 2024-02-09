import sys
import math
"""Proccess code"""
def interpret(filename):
    with open(filename) as file:
        for line in file:
            if ";add" in line:
                name, math = line.split(" ")
                num1, num2 = math.split("+")
                num1 = int(num1)
                num2 = int(num2)
                print(num1+num2)
            elif ";sub" in line:
                name, math = line.split(" ")
                num1, num2 = math.split("-")
                num1, num2 = int(num1), int(num2)
                print(num1-num2)
            elif ";mul" in line:
                name, math = line.split(" ")
                num1, num2 = math.split("*")
                num1, num2 = int(num1), int(num2)
                print(num1*num2)
            elif ";div" in line:
                name, math = line.split(" ")
                num1, num2 = math.split("/")
                num1, num2 = int(num1), int(num2)
                print(num1/num2)
            elif ";pow" in line:
                name, math = line.split(" ")
                num1, num2 = math.split("^")
                num1, num2 = int(num1), int(num2)
                print(num1**num2)
            elif "//;" in line:
                pass
            elif ";newline" in  line:
                print("\n")
            elif ";printf" in line:
                name, filename = line.split(" ")
                with open(filename) as file:
                    for line in file:
                        print(line)
            elif ";root" in line:
                name, math = line.split(" ")
                math = int(math)
                answer = math.sqrt(math)
                print(answer)
            else:
                print(line)

def shell():
    print("Welcome to the interactive shell. The Shell allows you to run commands\nexit() to exit")
    while True:
        shellinput = input(">> ")
        if shellinput == "exit()":
            return
        if shellinput == "sysexit()":
            sys.exit()
        elif len(shellinput) != 0 and shellinput != "exit()" and "sysexit()":
            if ";add" in shellinput:
                name, math = shellinput.split(" ")
                num1, num2 = math.split("+")
                num1 = int(num1)
                num2 = int(num2)
                print(num1+num2)
            elif "//;" in shellinput:
                pass
            elif ";sub" in shellinput:
                name, math = shellinput.split(" ")
                num1, num2 = math.split("-")
                num1 = int(num1)
                num2 = int(num2)
                print(num1-num2)
            elif ";mul" in shellinput:
                name, math = shellinput.split(" ")
                num1, num2 = math.split("*")
                num1, num2 = int(num1), int(num2)
                print(num1*num2)
            elif ";div" in shellinput:
                name, math = shellinput.split(" ")
                num1, num2 = math.split("/")
                num1, num2 = int(num1), int(num2)
                print(num1/num2)
            elif ";pow" in shellinput:
                name, math = shellinput.split(" ")
                num1, num2 = math.split("^")
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
                name, math = shellinput.split(" ")
                math = int(math)
                answer = math.sqrt(math)
                print(answer)
            else:
                print(shellinput)
        else:
            pass
