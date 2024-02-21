import turtle
from var import let, functioned
tur = turtle
"""Checks for Art module functions"""
def art(userinput):
    if userinput.startswith(";brush"):
        tur.Turtle()
    elif userinput.startswith(";brush.color"):
        name, color = userinput.split(" ")
        tur.color(color)
    