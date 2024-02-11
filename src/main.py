import interpreter
import sys

class main():
    """The main function"""
    def main():
        while True:
            inputuser = input("> ")
            if inputuser == "exit()":
                sys.exit()
                break
            elif inputuser == "license()":
                print(f"Text-Language Interpreter is licensed under a MIT License\nCopyright c 2024 Bruce Li\nPermission is hereby granted, free of charge, to any person obtaining a copy\nof this software and associated documentation files the Software, to deal\nin the Software without restriction, including without limitation the rights\nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell\ncopies of the Software, and to permit persons to whom the Software is\nfurnished to do so, subject to the following conditions:\nThe above copyright notice and this permission notice shall be included in all\ncopies or substantial portions of the Software.\nTHE SOFTWARE IS PROVIDED AS IS, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.")
            elif inputuser == "shell":
                interpreter.shell()
            try:
                interpreter.openfile(inputuser)
            except Exception as e:
                if len(inputuser) < 1 or inputuser == 'exit()' or inputuser == 'license()' or inputuser == 'shell':
                    pass
                else:
                    print(f"txt: An error occurred: {e}")
print("Text-Language Interpreter: TLI\nEnter filepath or start a shell session with shell.\nOr exit() to exit or license() for license.")
main.main()
