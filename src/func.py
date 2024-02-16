import math
def proccess(input):
    shellinput = input
    if ";add" in shellinput:
        try:
            name, mth = shellinput.split(" ")
            num1, num2 = mth.split("+")
            num1 = int(num1)
            num2 = int(num2)
            print(num1 + num2)
        except Exception as e:
            print(f"tldt: An error occured: {e}")
    elif "//;" in shellinput:
        pass
    elif ";sub" in shellinput:
        try:
            name, mth = shellinput.split(" ")
            num1, num2 = mth.split("-")
            num1 = int(num1)
            num2 = int(num2)
            print(num1 - num2)
        except Exception as e:
            print(f"tldt: An error occured: {e}")   
    elif ";mul" in shellinput:
        try:
            name, mth = shellinput.split(" ")
            num1, num2 = mth.split("*")
            num1, num2 = int(num1), int(num2)
            print(num1 * num2, end="")
        except Exception as e:
            print(f"tldt: An error occured: {e}")
    elif ";div" in shellinput:
        try:
            name, mth = shellinput.split(" ")
            num1, num2 = mth.split("/")
            num1, num2 = int(num1), int(num2)
            print(num1 / num2, end="")
        except Exception as e:
            print(f"tldt: An error occured: {e}")
    elif ";pow" in shellinput:
        try:
            name, mth = shellinput.split(" ")
            num1, num2 = mth.split("^")
            num1, num2 = int(num1), int(num2)
            print(num1**num2, end="")
        except Exception as e:
            print(f"tldt: An error occured: {e}")
    elif ";newline" in shellinput:
        print("\n")
    elif ";printf" in shellinput:
        try:
           name, filename = shellinput.split(" ")
           with open(filename) as file:
                for line in file:
                    print(line, end="")
        except Exception as e:
            print(f"tldt: An error occured: {e}")
    elif ";root" in shellinput:
        try:
            name, mth = shellinput.split(" ")
            mth = int(mth)
            answer = math.sqrt(mth)
            print(answer, end="")
        except Exception as e:
            print(f"tldt: An error occured: {e}")
    elif ";write:" in shellinput:
        try:
            name, content1 = shellinput.split(":")
            content, filename = content1.split("|filename|")
            with open(filename, "a") as file:
                file.write(content)
        except Exception as e:
            print(f"tldt: An error occured: {e}")
    elif ";overwrite:" in shellinput:
        try:
            name, content1 = shellinput.split(":")
            content, filename = content1.split("|filename|")
            with open(filename, "w") as file:
                file.write(content)
        except Exception as e:
            print(f"tldt: An error occured: {e}")
    elif ";sqr" in shellinput:
         try:
            name, math = shellinput.split(" ")
            math = int(math)
            print(math**2, end="")
         except Exception as e:
             print(f"tldt: An error occured: {e}")    
    else:
        print(shellinput, end="")
 
