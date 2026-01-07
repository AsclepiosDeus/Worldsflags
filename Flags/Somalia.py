import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Bases.Shapes import *

hideturtle()

couleurs= ['#4189DD']
for c in couleurs:
    rectangle(c,300,200)
    forward(100)

left(90)
forward(100)
left(-90)
forward(50)

right(54)
star('#FFFFFF',5,-108,50)
right(-54)

up()
goto(0,0) 
down()

outline('black', 300,200) 

mainloop()  