
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
        cb = str(userinput)
        return str(cb)
