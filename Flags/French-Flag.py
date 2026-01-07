import sys
import os

# Ajoute le dossier parent (Worldsflags) au chemin d'import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Bases.Shapes import *

hideturtle()

couleurs= ['#000091', 'white', '#E1000F']
for c in couleurs:
    rectangle(c,100,200)
    forward(100)

up()
goto(0,0) 
down()
contour('black', 300,200) 
mainloop()  