from turtle import *
from math import *

def rectangle(coul,a,b):
    color(coul)
    begin_fill()
    for i in range(2):
        forward(a)
        left(90)
        forward(b)
        left(90)
    end_fill()

def outline(coul,a,b):
    color(coul)
    for i in range(2):
        forward(a)
        left(90)
        forward(b)
        left(90)
        
def star(coul,n,angle,rayon):
    up()
    color(coul)
    taille=rayon/(sin(radians(angle/2)) / sin(radians(180/n)))
    forward(rayon)
    left(angle/2+180/n)
    down()
    begin_fill()
    for i in range(n):
        forward(taille)
        left(180-angle)
        forward(taille)
        right(180-(360/n+angle))
    end_fill()
    up()
    left(-angle/2-180/n)
    forward(-rayon)
    
def poly_point(coul, n, rayon):
    color(coul)
    up()
    forward(rayon)
    left(180-(180/2-180/n))
    for i in range(n):
        dot(10) #dessine un point de diamètre 10 pixels
        forward(2*rayon*sin(pi/n))
        left(360/n)
        
    right(180-(180/2-180/n))
        
def poly_star(coul, n, rayon):
    color(coul)
    up()
    forward(rayon)
    left(180-(180/2-180/n))
    for i in range(n):
        cap=heading()
        setheading(0)
        left(54)
        etoile(coul,4,108,4)
        right(54)
        setheading(cap)
        forward(2*rayon*sin(pi/n))
        left(360/n)
        
    right(180-(180/2-180/n))
    
def isosceles(coul,base,hauteur):
    color(coul)
    begin_fill()
    forward(base)
    iso=sqrt((base/2)**2+hauteur**2)
    angle_iso=degrees(atan(hauteur/(base/2)))
    left(180-angle_iso)
    forward(iso)
    left(180-(180-2*angle_iso))
    forward(iso)
    left(180-angle_iso)
    end_fill()
    
def circle(coul, rayon, angle=360):
    color(coul)
    right(90)
    forward(rayon)
    left(90)
    begin_fill()
    circle(rayon,extent = angle)
    left(90)
    forward(rayon)
    right(90)
    end_fill()
    
def tri_rectangle(coul,base,hauteur):
    color(coul)
    angle_b=degrees(atan(hauteur/base))
    angle_h=degrees(atan(base/hauteur))
    hyp=sqrt(base**2+hauteur**2)
    begin_fill()
    forward(base)
    left(180-angle_b)
    forward(hyp)
    left(180-angle_h)
    forward(hauteur)
    left(90)
    end_fill()