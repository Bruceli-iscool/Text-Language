import sys
from io import StringIO
import func
from interpreter import var

def var_process(userinput):        
    if "{" in userinput:
            try:
                # redirect output
                other = userinput.split("{")
                varstr = other.split("}")
                original_output = sys.stdout
                sys.stdout = output = StringIO()
                try:
                    func.proccess(var[varstr[1:]])
                finally:
                    sys.stdout = original_output
                    actual_output = output.getvalue().strip()
                    if actual_output:
                        return actual_output
            except Exception as e:
                print(f"tldt: An error occured: {e}")
    else:
         return userinput