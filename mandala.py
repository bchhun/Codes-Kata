#coding: utf-8

"""
    http://eric_rollins.home.mindspring.com/introProgramming/hw2.html

    2.1 Setup

    Utilisation de Tkinter au lieu de livewires (deprecated)
"""

from Tkinter import *
import math

class DerivedCanvas(Canvas):
    """
        Héritage de Canvas pour me permettre de dessiner des cercles
        avec des paramètres simples
    """
    def create_circle(self, x, y, radius, fill = None, outline = None, width = 0):

        return self.create_oval(
            x - radius, y - radius, x + radius, y + radius
            , width=width, fill=fill, outline=outline
        )

def draw_circle_within_rectange():
    """
        2.2 Start drawing
    """
    master = Tk()

    w = DerivedCanvas(master, width=400, height=400)
    w.pack()

    circle = w.create_circle( x=100, y=100, radius=50, fill=None, outline="black", width=1)
    rectangle = w.create_rectangle(50, 50, 200, 200, outline="blue", fill=None, width=1) 

    mainloop()

def point_on_circle(x, y, radius, angle):
    new_x = (float)(radius * math.cos(angle * math.pi / 180)) + x
    new_y = (float)(radius * math.sin(angle * math.pi / 180)) + y

    return (new_x, new_y)

def draw_simple_mandala(x, y, radius):
    """
        2.3 Nested functions

        Your next objective is to draw a mandala, using nested function calls.

        You will have a base function, which may call a second and third to perform nested levels of drawing.

        The functions will accept coordinates and radius as arguments and draw boxes and circles at different locations on the screen.
    """
    master = Tk()
    w = DerivedCanvas(master, width=600, height=600)
    w.pack()

    # cercle centrale
    w.create_circle(x=x, y=y, radius=radius, fill=None, outline="red", width=1)
    
    #polygone interne #1
    coordinates = [x - radius, y, x, y - radius, x + radius, y, x, y + radius]
    w.create_polygon(coordinates, outline="blue", fill="blue", width=1)

    print point_on_circle(x, y, radius, 0.45)


def main():
    draw_simple_mandala(x=300, y=300, radius=175)

if __name__ == '__main__':
    main()