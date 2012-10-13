#coding: utf-8

"""
    http://eric_rollins.home.mindspring.com/introProgramming/hw2.html

    2.1 Setup

    Utilisation de Tkinter au lieu de livewires (deprecated)
"""

from Tkinter import *

class DerivedCanvas(Canvas):
    def create_circle(self):
        """
            2.2 Start drawing
        """

        print "create_circle"

def main():
    master = Tk()

    w = DerivedCanvas(master, width=400, height=400)
    w.pack()
    w.create_circle()

    mainloop()

if __name__ == '__main__':
    main()