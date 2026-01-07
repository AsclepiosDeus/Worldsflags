import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Bases.Shapes import *

hideturtle()

couleurs= ['#008C45', '#F4F9FF', '#CD212A']
for c in couleurs:
    rectangle(c,100,200)
    forward(100)

up()
goto(0,0) 
down()

outline('black', 300,200) 

mainloop()  