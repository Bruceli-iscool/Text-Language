from var import let, functioned
import interpreter
import var_pro
import sys
from io import StringIO
import random

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
                num1 = var_pro.var_pro(num1, let)
                num2 = var_pro.var_pro(num2, let)
                num1 = float(num1)
                num2 = float(num2)
                print(num1 + num2)
            except Exception as e:
                print(f"tldt: An error occurred: {e}")
        elif "//;" in userinput:
            pass
        elif userinput.startswith(";sub"):
            try:
                name, mth = userinput.split(" ")
                num1, num2 = mth.split("-")
                num1 = var_pro.var_pro(num1, let)
                num2 = var_pro.var_pro(num2, let)
                num1 = float(num1)
                num2 = float(num2)
                print(num1 - num2)
            except Exception as e:
                print(f"tldt: An error occurred: {e}")
        elif userinput.startswith(";mul"):
            try:
                name, mth = userinput.split(" ")
                num1, num2 = mth.split("*")
                num1 = var_pro.var_pro(num1, let)
                num2 = var_pro.var_pro(num2, let)
                num1, num2 = float(num1), float(num2)
                print(num1 * num2)
            except Exception as e:
                print(f"tldt: An error occurred: {e}")
        elif userinput.startswith(";div"):
            try:
                name, mth = userinput.split(" ")
                num1, num2 = mth.split("/")
                num1 = var_pro.var_pro(num1, let)
                num2 = var_pro.var_pro(num2, let)
                num1, num2 = float(num1), float(num2)
                print(num1 / num2)
            except Exception as e:
                print(f"tldt: An error occurred: {e}")
        elif userinput.startswith(";pow"):
            try:
                name, mth = userinput.split(" ")
                num1, num2 = mth.split("^")
                num1 = var_pro.var_pro(num1, let)
                num2 = var_pro.var_pro(num2, let)
                num1, num2 = float(num1), float(num2)
                print(num1**num2)
            except Exception as e:
                print(f"tldt: An error occurred: {e}")
        elif userinput.startswith(";newline"):
            print("\n")
        elif userinput.startswith(";printf"):
            try:
                name, filename = userinput.split(" ")
                filename = var_pro.var_pro(filename, let)
                with open(filename) as file:
                    for line in file:
                        print(line)
            except Exception as e:
                print(f"tldt: An error occured: {e}")
        elif userinput.startswith(";root"):
            try:
                name, mth = userinput.split(" ")
                mth = float(mth)
                mth = var_pro.var_pro(mth, let)
                answer = math.sqrt(mth)
                print(answer, end="")
            except Exception as e:
                print(f"tldt: An error occured: {e}")
        elif userinput.startswith(";write~"):
            try:
                name, content1 = userinput.split("~")
                content, filename = content1.split("|filename|")
                filename = var_pro.var_pro(filename, let)
                content = var_pro.var_pro(content, let)
                with open(filename, "a") as file:
                    file.write(content)
            except Exception as e:
                print(f"tldt: An error occured: {e}")
        elif userinput.startswith(";overwrite~"):
            try:
                name, content1 = userinput.split("~")
                content, filename = content1.split("|filename|")
                filename = var_pro.var_pro(filename, let)
                content = var_pro.var_pro(content, let)
                with open(filename, "w") as file:
                    file.write(content)
            except Exception as e:
                print(f"tldt: An error occured: {e}")
        elif userinput.startswith(";") and userinput[1:] in functioned:
            action = functioned[userinput[1:]]
            try:
                action, action2, action3, action4, action5 = action.split(":")
                interpreter.interpret(action)
                interpreter.interpret(action2)
                interpreter.interpret(action3)
                interpreter.interpret(action4)
                interpreter.interpret(action5)
            except Exception:
                try:
                    action, action2, action3, action4 = action.split(":")
                    interpreter.interpret(action)
                    interpreter.interpret(action2)
                    interpreter.interpret(action3)
                    interpreter.interpret(action4)
                except Exception:
                    try:
                        action, action2, action3 = action.split(":")
                        interpreter.interpret(action)
                        interpreter.interpret(action2)
                        interpreter.interpret(action3)
                    except Exception:
                        try:
                            action, action2 = action.split(":")
                            interpreter.interpret(action)
                            interpreter.interpret(action2)
                        except Exception:
                            interpreter.interpret(action)
        elif userinput.startswith(";sqr"):
            try:
                name, math = line.split(" ")
                math = float(math)
                math = var_pro.var_pro(math, let)
                print(math**2)
            except Exception as e:
                print(f"tldt: An error occured: {e}")
        elif userinput.startswith(";prompt"):
            try:
                name, prompt = userinput.split(">")
                ask, vartostore = prompt.split(":")
                answer = str(input(ask))
                let[vartostore] = '"'+answer+'"'
            except Exception as e:
                print(f"tldt: An error occured: {e}")
        elif ";if" in userinput:
            try:
                name, other = userinput.split(">")
                cCB2, otherCB = other.split("|")
                if "==" in cCB2:
                    conv1, cCB2 = cCB2.split("==")
                    conv1 = var_pro.var_pro(conv1, let)
                    cCB2 = var_pro.var_pro(cCB2, let)
                    if conv1 == cCB2:
                        try:
                            code1, code2, code3, code4, code5 = otherCB.split(":")
                            interpreter.interpret(code1)
                            interpreter.interpret(code2)
                            interpreter.interpret(code3)
                            interpreter.interpret(code4)
                            interpreter.interpret(code5)
                        except Exception:
                            try:
                                code1, code2, code3, code4 = otherCB.split(":")
                                interpreter.interpret(code1)
                                interpreter.interpret(code2)
                                interpreter.interpret(code3)
                                interpreter.interpret(code4)
                            except Exception:
                                try:
                                    code1, code2, code3 = otherCB.split(":")
                                    interpreter.interpret(code1)
                                    interpreter.interpret(code2)
                                    interpreter.interpret(code3)
                                except Exception:
                                    try:
                                        code1, code2 = otherCB.split(":")
                                        interpreter.interpret(code1)
                                        interpreter.interpret(code2)
                                    except Exception:
                                        try:
                                            interpreter.interpret(otherCB)
                                        except Exception as e:
                                            print("tldt: Not enough arguments.")
                elif ">" in cCB2:
                    conv1, cCB2 = cCB2.split(">")
                    conv1 = float(var_pro.var_pro(conv1, let))
                    cCB2 = float(var_pro.var_pro(cCB2, let))
                    if conv1 > cCB2:
                        try:
                            code1, code2, code3, code4, code5 = otherCB.split(":")
                            interpreter.interpret(code1)
                            interpreter.interpret(code2)
                            interpreter.interpret(code3)
                            interpreter.interpret(code4)
                            interpreter.interpret(code5)
                        except Exception:
                            try:
                                code1, code2, code3, code4 = otherCB.split(":")
                                interpreter.interpret(code1)
                                interpreter.interpret(code2)
                                interpreter.interpret(code3)
                                interpreter.interpret(code4)
                            except Exception:
                                try:
                                    code1, code2, code3 = otherCB.split(":")
                                    interpreter.interpret(code1)
                                    interpreter.interpret(code2)
                                    interpreter.interpret(code3)
                                except Exception:
                                    try:
                                        code1, code2 = otherCB.split(":")
                                        interpreter.interpret(code1)
                                        interpreter.interpret(code2)
                                    except Exception:
                                        interpreter.interpret(otherCB)
                elif "<" in cCB2:
                    conv1, cCB2 = cCB2.split("<")
                    conv1 = float(var_pro.var_pro(conv1, let))
                    cCB2 = float(var_pro.var_pro(cCB2, let))
                    if conv1 < cCB2:
                        try:
                            code1, code2, code3, code4, code5 = otherCB.split(":")
                            interpreter.interpret(code1)
                            interpreter.interpret(code2)
                            interpreter.interpret(code3)
                            interpreter.interpret(code4)
                            interpreter.interpret(code5)
                        except Exception:
                            try:
                                code1, code2, code3, code4 = otherCB.split(":")
                                interpreter.interpret(code1)
                                interpreter.interpret(code2)
                                interpreter.interpret(code3)
                                interpreter.interpret(code4)
                            except Exception:
                                try:
                                    code1, code2, code3 = otherCB.split(":")
                                    interpreter.interpret(code1)
                                    interpreter.interpret(code2)
                                    interpreter.interpret(code3)
                                except Exception:
                                    try:
                                        code1, code2 = otherCB.split(":")
                                        interpreter.interpret(code1)
                                        interpreter.interpret(code2)
                                    except Exception:
                                        interpreter.interpret(otherCB)
                elif "!=" in cCB2:
                    conv1, cCB2 = cCB2.split("!=")
                    conv1 = var_pro.var_pro(conv1, let)
                    cCB2 = var_pro.var_pro(cCB2, let)
                    if conv1 != cCB2:
                        try:
                            code1, code2, code3, code4, code5 = otherCB.split(":")
                            interpreter.interpret(code1)
                            interpreter.interpret(code2)
                            interpreter.interpret(code3)
                            interpreter.interpret(code4)
                            interpreter.interpret(code5)
                        except Exception:
                            try:
                                code1, code2, code3, code4 = otherCB.split(":")
                                interpreter.interpret(code1)
                                interpreter.interpret(code2)
                                interpreter.interpret(code3)
                                interpreter.interpret(code4)
                            except Exception:
                                try:
                                    code1, code2, code3 = otherCB.split(":")
                                    interpreter.interpret(code1)
                                    interpreter.interpret(code2)
                                    interpreter.interpret(code3)
                                except Exception:
                                    try:
                                        code1, code2 = otherCB.split(":")
                                        interpreter.interpret(code1)
                                        interpreter.interpret(code2)
                                    except Exception:
                                        interpreter.interpret(otherCB)
            except Exception as e:
                print(f"tldt: An error occured: {e}")
        elif userinput.startswith(";choice"):
            try:
                name, content = userinput.split(">")
                random1, cbrandom, varname = content.split(",")
                random1 = int(var_pro.var_pro(random1, let))
                cbrandom = int(var_pro.var_pro(cbrandom, let))
                let[varname] = random.randint(random1, cbrandom)
            except Exception as e:
                print(f"tldt: An error occured: {e}")
        elif userinput.startswith(";while"):
            try:
                name, funtion = userinput.split(">")
                cbname, functioncb = funtion.split(":")
                while cbname:
                    interpreter.interpret(functioncb)
            except Exception as e:
                print(f"tldt: An error occured: {e}")
        elif userinput.startswith(";break"):
            sys.exit()
        elif userinput.startswith(";int"):
            try:
                name, variable = userinput.split(">")
                var = var_pro.var_pro(variable, let)
                var, decimal = var.split(".")
                let[variable]=var
            except Exception as e:
                print(f"tldt: An error occured: {e}")
        elif userinput.startswith(";join"):
            try:
                name, cb1 = userinput.split(">")
                cb2, cb3 = cb1.split("=")
                cb, cb5 = cb2.split("+")
                cb = var_pro.var_pro(cb, let)
                cb5 = var_pro.var_pro(cb5, let)
                let[cb3] = cb + cb5
            except Exception as e:
                print(f"tldt: An error occured: {e}")
        elif "[" in userinput:
            try:
                # redirect output
                sentence, other = userinput.split("[")
                varstr, sentence2 = other.split("]")
                original_output = sys.stdout
                sys.stdout = output = StringIO()
                try:
                    interpreter.interpret(vars[varstr[1:]])
                finally:
                    sys.stdout = original_output
                    actual_output = output.getvalue().strip()
                    if actual_output:
                        print(sentence + actual_output + sentence2)
            except Exception as e:
                print(f"tldt: An error occured: {e}")
        else:
            userinput = var_pro.var_pro(userinput, let)
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
