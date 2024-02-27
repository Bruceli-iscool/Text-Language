# Variables in Text-Language

Variables can be declared like this:

    ;var>varname="varvalue"
    ;var>varname=;add 1+2

They can be used in formated strings:

    1+2 = [;varname] and thats it
    //; returns 1+2 = 3 and thats it
They can be declared with the let keyword:
    ;let>hi=43
    ;add {hi}+4
