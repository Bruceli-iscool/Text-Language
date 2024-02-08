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
            else:
                print(line)

def shell():
    print("Welcome to the interactive shell. The Shell allows you to run commands\nexit() to exit")
    while True:
        shellinput = input(">> ")
        if shellinput == "exit()":
            return
        elif len(shellinput) != 0 and shellinput != "exit()":
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
            else:
                print(shellinput)
        else:
            pass
