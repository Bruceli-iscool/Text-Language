import sys
import math
import re
import func
from io import StringIO

"""Proccess code"""

# list of functions
functioned = {}
# list of variables
vars = {}
# work on TDLI error handling
let = {}


# make all in into startswith()
# always write elifs before the "{" check line in interpret
def var_pro(userinput, c):
    if "{" in userinput and "}" in userinput:
        start = userinput.find("{") + 1
        end = userinput.find("}")
        if start < end:
            var = userinput[start:end]
            var = var.rstrip()
        if var in c:
            action = c[var[0:]]
            action = str(action)
            return str(action)
        else:
            print(f"tldt: Variable '{var[0:]}' not found")
            return userinput
    else:
        return userinput


def interpret(userinput):
    if (
        ";define" not in userinput
        and ";var" not in userinput
        and ";let" not in userinput
    ):
        if userinput.startswith(";add"):
            try:
                name, mth = userinput.split(" ")
                num1, num2 = mth.split("+")
                num1 = var_pro(num1, let)
                num2 = var_pro(num2, let)
                num1 = int(num1)
                num2 = int(num2)
                print(num1 + num2)
            except Exception as e:
                print(f"tldt: An error occurred: {e}")
        elif "//;" in userinput:
            pass
        elif ";sub" in userinput:
            try:
                name, mth = userinput.split(" ")
                num1, num2 = mth.split("-")
                num1 = var_pro(num1, let)
                num2 = var_pro(num2, let)
                num1 = int(num1)
                num2 = int(num2)
                print(num1 - num2)
            except Exception as e:
                print(f"tldt: An error occurred: {e}")
        elif ";mul" in userinput:
            try:
                name, mth = userinput.split(" ")
                num1, num2 = mth.split("*")
                num1 = var_pro(num1, let)
                num2 = var_pro(num2, let)
                num1, num2 = int(num1), int(num2)
                print(num1 * num2)
            except Exception as e:
                print(f"tldt: An error occurred: {e}")
        elif ";div" in userinput:
            try:
                name, mth = userinput.split(" ")
                num1, num2 = mth.split("/")
                num1 = var_pro(num1, let)
                num2 = var_pro(num2, let)
                num1, num2 = int(num1), int(num2)
                print(num1 / num2)
            except Exception as e:
                print(f"tldt: An error occurred: {e}")
        elif ";pow" in userinput:
            try:
                name, mth = userinput.split(" ")
                num1, num2 = mth.split("^")
                num1 = var_pro(num1, let)
                num2 = var_pro(num2, let)
                num1, num2 = int(num1), int(num2)
                print(num1**num2)
            except Exception as e:
                print(f"tldt: An error occurred: {e}")
        elif ";newline" in userinput:
            print("\n")
        elif ";printf" in userinput:
            try:
                name, filename = userinput.split(" ")
                filename = var_pro(filename, let)
                with open(filename) as file:
                    for line in file:
                        print(line)
            except Exception as e:
                print(f"tldt: An error occured: {e}")
        elif ";root" in userinput:
            try:
                name, mth = userinput.split(" ")
                mth = int(mth)
                mth = var_pro(mth, let)
                answer = math.sqrt(mth)
                print(answer, end="")
            except Exception as e:
                print(f"tldt: An error occured: {e}")
        elif userinput.startswith(";write~"):
            try:
                name, content1 = userinput.split("~")
                content, filename = content1.split("|filename|")
                filename = var_pro(filename, let)
                content = var_pro(content, let)
                with open(filename, "a") as file:
                    file.write(content)
            except Exception as e:
                print(f"tldt: An error occured: {e}")
        elif userinput.startswith(";overwrite~"):
            try:
                name, content1 = userinput.split("~")
                content, filename = content1.split("|filename|")
                filename = var_pro(filename, let)
                content = var_pro(content, let)
                with open(filename, "w") as file:
                    file.write(content)
            except Exception as e:
                print(f"tldt: An error occured: {e}")
        elif userinput.startswith(";") and userinput[1:] in functioned:
            action = functioned[userinput[1:]]
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
        elif userinput.startswith(";sqr"):
            try:
                name, math = line.split(" ")
                math = int(math)
                math = var_pro(math)
                print(math**2)
            except Exception as e:
                print(f"tldt: An error occured: {e}")
        elif userinput.startswith(";prompt"):
            try:
                name, prompt = userinput.split(">")
                ask, vartostore = prompt.split(":")
                answer = input(ask)
                let[vartostore] = answer
            except Exception as e:
                print(f"tldt: An error occured: {e}")
        elif userinput.startswith(";if"):
            try:
                name, other = userinput.split(">")
                conv1, cCB2 = other.split("=")
                cCB2, otherCB = cCB2.split("|")
                conv1 = var_pro(conv1)
                cCB2 = var_pro(cCB2)
                if "==" in other:
                    if conv1 == cCB2:
                        try:
                            code1, code2, code3, code4, code5 = otherCB.split(":")
                            func.proccess(code1)
                            func.proccess(code2)
                            func.proccess(code3)
                            func.proccess(code4)
                            func.proccess(code5)
                        except Exception:
                            try:
                                code1, code2, code3, code4 = otherCB.split(":")
                                func.proccess(code1)
                                func.proccess(code2)
                                func.proccess(code3)
                                func.proccess(code4)
                            except Exception:
                                try:
                                    code1, code2, code3 = otherCB.split(":")
                                    func.proccess(code1)
                                    func.proccess(code2)
                                    func.proccess(code3)
                                except Exception:
                                    try:
                                        code1, code2 = otherCB.split(":")
                                        func.proccess(code1)
                                        func.proccess(code2)
                                    except Exception:
                                        func.proccess(otherCB)
                elif ">" in other:
                    if conv1 > cCB2:
                        try:
                            code1, code2, code3, code4, code5 = otherCB.split(":")
                            func.proccess(code1)
                            func.proccess(code2)
                            func.proccess(code3)
                            func.proccess(code4)
                            func.proccess(code5)
                        except Exception:
                            try:
                                code1, code2, code3, code4 = otherCB.split(":")
                                func.proccess(code1)
                                func.proccess(code2)
                                func.proccess(code3)
                                func.proccess(code4)
                            except Exception:
                                try:
                                    code1, code2, code3 = otherCB.split(":")
                                    func.proccess(code1)
                                    func.proccess(code2)
                                    func.proccess(code3)
                                except Exception:
                                    try:
                                        code1, code2 = otherCB.split(":")
                                        func.proccess(code1)
                                        func.proccess(code2)
                                    except Exception:
                                        func.proccess(otherCB)
                elif "<" in other:
                    if conv1 < cCB2:
                        try:
                            code1, code2, code3, code4, code5 = otherCB.split(":")
                            func.proccess(code1)
                            func.proccess(code2)
                            func.proccess(code3)
                            func.proccess(code4)
                            func.proccess(code5)
                        except Exception:
                            try:
                                code1, code2, code3, code4 = otherCB.split(":")
                                func.proccess(code1)
                                func.proccess(code2)
                                func.proccess(code3)
                                func.proccess(code4)
                            except Exception:
                                try:
                                    code1, code2, code3 = otherCB.split(":")
                                    func.proccess(code1)
                                    func.proccess(code2)
                                    func.proccess(code3)
                                except Exception:
                                    try:
                                        code1, code2 = otherCB.split(":")
                                        func.proccess(code1)
                                        func.proccess(code2)
                                    except Exception:
                                        func.proccess(otherCB)
            except Exception as e:
                pass
        elif "[" in userinput:
            try:
                # redirect output
                sentence, other = userinput.split("[")
                varstr, sentence2 = other.split("]")
                original_output = sys.stdout
                sys.stdout = output = StringIO()
                try:
                    func.proccess(vars[varstr[1:]])
                finally:
                    sys.stdout = original_output
                    actual_output = output.getvalue().strip()
                    if actual_output:
                        print(sentence + actual_output + sentence2)
            except Exception as e:
                print(f"tldt: An error occured: {e}")
        else:
            userinput = var_pro(userinput)
            print(userinput)
    elif ";define" in userinput:
        try:
            name, content = userinput.split(">")
            funcname, action = content.split("=")
            functioned[funcname] = action
        except Exception as e:
            print(f"tldt: An error occured: {e}")
    elif ";var" in userinput:
        try:
            name, content = userinput.split(">")
            varname, value = content.split("=")
            vars[varname] = value
        except Exception as e:
            print(f"tldt: An error occured: {e}")
    elif ";let" in userinput:
        try:
            name, content = userinput.split(">")
            varname, value = content.split("=")
            let[varname] = value
        except Exception as e:
            print(f"tldt: An error occured: {e}")
    else:
        pass


def openfile(filename):
    with open(filename) as file:
        for line in file:
            if "#get" in line:
                try:
                    name, filepath = line.split(" ")
                    with open(filepath) as filename:
                        for line in filename:
                            line = line.rstrip("\n")
                            line = str(line)
                            interpret(line)
                except Exception as e:
                    print(f"tldt: An error occured: {e}")
            else:
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
        elif len(shellinput) < 2:
            pass
        if "#get" in shellinput:
            try:
                name, filepath = shellinput.split(" ")
                with open(filepath) as filename:
                    for line in filename:
                        line = str(line)
                        interpret(line)
            except Exception as e:
                print(f"tldt: An error occured: {e}")
        elif shellinput != "":
            interpret(shellinput)
