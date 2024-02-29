import var_pro
from var import *

"""String Operations for Text-Language"""

def check(userinput):
    if userinput.startswith(";upcase"):
        try:
            name, other = userinput.split(">")
            vartosplit, vartostore = other.split("=")
            vartosplit = var_pro.var_pro(vartosplit, let)
            result = vartosplit.upper()
            let[vartostore] = result
            return 1
        except Exception as e:
            print(f"tldt: An error occured: {e}")
    else:
        return 0