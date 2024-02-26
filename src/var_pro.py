"""def var_pro(userinput, c):
    if "{" in userinput and "}" in userinput:
        var = userinput.split("{")[1].split("}")[0].rstrip()
        if var in c:
            action = c[var]
            action = str(action)
            if "+" or "-" or "/" or "*" in action:
                if "+" in action:
                    try:
                        num1, num2 = action.split("+")
                        num1 = float(num1)
                        num2 = float(num2)
                        sum = num1 + num2
                        return str(sum)
                    except Exception as e:
                        print(f"tldt: An error occured: {e}")
                elif "-" in action:
                    try:
                       num1, num2 = action.split("-")
                       num1 = float(num1)
                       num2 = float(num2)
                       diff = num1 -  num2
                       return str(diff)
                    except Exception as e:
                        print(f"tldt: An error occured: {e}")
                elif "/" in action:
                    try:
                       num1, num2 = action.split("/")
                       num1 = float(num1)
                       num2 = float(num2)
                       diff = num1 / num2
                       return str(diff)
                    except Exception as e:
                        print(f"tldt: An error occured: {e}")
                elif "*" in action:
                    try:
                       num1, num2 = action.split("*")
                       num1 = float(num1)
                       num2 = float(num2)
                       diff = num1 *  num2
                       return str(diff)
                    except Exception as e:
                        print(f"tldt: An error occured: {e}")
            else:
                action = str(action)
                return action
            print(f"tldt: Variable '{var[0:]}' not found")
            return userinput
    else:
        return userinput"""
def var_pro(userinput, c):
    if "{" in userinput and "}" in userinput:
        start_index = userinput.find("{") + 1
        end_index = userinput.find("}")
        var = userinput[start_index:end_index].strip()

        if var in c:
            try:
                result = eval(str(c[var]))
                return userinput.replace(f"{{{var}}}", str(result))
            except Exception as e:
                print(f"tldt: An error occurred: {e}")
                return userinput
        else:
            print(f"tldt: Variable '{var}' not found")
            return userinput
    else:
        return userinput
