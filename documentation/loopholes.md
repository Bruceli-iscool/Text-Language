# loopholes

In Text-Language there is limited syntax features. It lacks features like functions with arguments, else statements, or orderly syntax. 
Bypass args restriction:

        //; I have a function that adds two varibables.
        //; have user declare variables first
        ;let>num1=2
        ;let>num2=4
        //; use these two variables in function
        ;define>domath=;add {num1}+{num2}

Bypass lack of else staements:

        //; detect if 0 equals 0 otherwise print false
        ;if>0==0|true
        //; use not equal instead of else loop
        ;if>0!=0|false