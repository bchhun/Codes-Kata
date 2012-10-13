#coding: utf-8

"""
    http://eric_rollins.home.mindspring.com/introProgramming/hw2.html

    2.1 Setup

    Utilisation de Tkinter au lieu de livewires (deprecated)
"""

from Tkinter import *

class DerivedCanvas(Canvas):
    """
        Héritage de Canvas pour me permettre de dessiner des cercles
        avec des paramètres simples
    """
    def create_circle(self, x, y, radius, fill = None, outline = None):
        """
            2.2 Start drawing

        """
        return self.create_oval(x - radius, y - radius, x + radius, y + radius, width=0, fill=fill, outline=outline)

def main():
    master = Tk()

    w = DerivedCanvas(master, width=400, height=400)
    w.pack()
    
    text = w.create_text(50,10, text="tk test")
    circle = w.create_circle(100, 100, 20, None, "black")

    mainloop()

if __name__ == '__main__':
    main()