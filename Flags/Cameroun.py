import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Bases.Shapes import *

hideturtle()
couleurs= [ '#007A5E'  , '#CE1126', '#FCD116'] #vert, rouge, jaune
for c in couleurs:
    rectangle(c,100,200)
    forward(100)

up()
goto(150,100) 
down()

left(54)
star('#FCD116',5,36,10)
right(54)

up()
goto(0,0) 
down()
outline('black', 300,200) 
mainloop()