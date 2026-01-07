import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Bases.Shapes import *

hideturtle()

couleurs= ['#2D2926', '#FFCD00', '#C8102E']
for c in couleurs:
    rectangle(c,100,200)
    forward(100)

up()
goto(0,0) 
down()

outline('black', 300,200) 

mainloop()  