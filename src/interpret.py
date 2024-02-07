import sys
"""Proccess code"""
def interpret(filename):
    with open(filename) as file:
        for line in file:
            print(line)

def shell():
    print("Welcome to the interactive shell. The Shell allows you to run commands\nexit() to exit")
    while True:
        shellinput = input(">> ")
        if shellinput == "exit()":
            return
        elif len(shellinput) != 0 and shellinput != "exit()":
            print(shellinput)  
        else:
            pass
