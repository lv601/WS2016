# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 22:28:46 2016

@author: jose
"""
"""
Kompensationsaufgabe Basílio José

Erstellen Sie eine weitere Klasse "Tree", die genauso aufgebaut ist wie die Klasse "House" und ebenfalls von MyTurtle
abgeleitet wird.

Desweiteren erstellen Sie eine Klasse "Town", der Sie mehrere Objekte vom Typ "MyTurtle" oder "Town" übergeben können
(*args). Die Klasse "Town" soll alle übergebenen Objekte zeichen, wenn die Instanz als Funktion aufgerufen wird.
Verwenden Sie hierfür die __call__() Methode.

Implementieren Sie die noch fehlenden Methoden __radd__(), __iadd__(), __rmul__(), __imul__() und __getitem__() der
Klasse "Town".

Implementieren Sie die noch fehlenden Methoden __add__(), __rmul__() der Basisklasse "MyTurtle". Wobei __rmul__() einen
Integer erwartet und __add__ eine Instanz der Klasse "MyTurtle". Alle liefern ein Objekt der Klasse "Town" zurück.
"""
#!/usr/bin/env python3

import turtle
import math
import itertools

class MyTurtle:
    def __call__(self):
        self.draw()

    def __mul__(self, other):
        if isinstance(other, int):
            multiple = list(itertools.repeat(self, other))
            return Town(*multiple)
        else:
            return NotImplementend

    def __rmul__(self, other):
       if isinstance(other, int):
           return MyTurtle.__mul__(self, other)
       else:
           return NotImplemented

    def __add__(self, other):
        if isinstance(other, MyTurtle):
            self.append(other)
            return Town(*self)
        else:
            NotImplemented

    # Overwrite in sub classes
    def draw(self):
        raise NotImplementedError


class House(MyTurtle):
    def __init__(self, length, levels):
        self.levels = levels
        self.length = length

    def draw(self):
        pos = turtle.pos()

        for i in range(self.levels):
            self._draw_level()

        self._draw_roof()

        pos = (pos[0] + self.length, pos[1])

        turtle.penup()
        turtle.setpos(pos)
        turtle.pendown()


    def _draw_level(self):
        pos = turtle.pos()

        for i in range(4):
            turtle.forward(self.length)
            turtle.left(90)

        turtle.penup()
        turtle.sety(pos[1] + self.length)
        turtle.pendown()

    def _draw_roof(self):
        pos = turtle.pos()

        get_hypotenuse = math.sqrt(((self.length / 2) ** 2) * 2)
        turtle.left(45)
        turtle.forward(get_hypotenuse)
        turtle.right(90)
        turtle.forward(get_hypotenuse)
        turtle.penup()
        turtle.setpos(pos)
        turtle.pendown()
        turtle.left(45)


class Tree(MyTurtle):
    def __init__(self, length, count_trees):
        self.count_trees = count_trees
        self.length = length
        pass

    def draw(self):
        pos = turtle.pos()
    
        # Stem
        turtle.forward(5)
        turtle.left(90)
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(5)
        turtle.left(90)
        turtle.forward(10)
        turtle.left(180)

        # Go to position where the treetop is painted
        turtle.penup()
        turtle.forward(10)
        turtle.right(90)
        turtle.forward(2.5)
        turtle.pendown()

        # Treetop
        turtle.circle(10)

        pos = (pos[0] + self.length, pos[1])

        turtle.penup()
        turtle.setpos(pos)
        turtle.pendown()



class Town():
    def __init__(self, *args):
        self.turtles = []
        raise NotImplementedError

    def __call__(self):
        raise NotImplementedError

    def __add__(self, other):
        if isinstance(other, MyTurtle):
            self.turtles.append(other)
            return Town(*self.turtles)
        elif isinstance(other, Town):
            self.turtles.extend(other.turtles)
            return Town(*self.turtles)
        else:
            return NotImplemented

    def __radd__(self, other):
        if isinstance(other, MyTurtle) or isinstance(other, Town):
            return Town.__add__(self, other)
        else:
            return NotImplemented

    def __iadd__(self, other):
       if isinstance(other, MyTurtle):
           self.turtles.append(other)
           return Town(*self.turtles)
       elif isinstance(other, Town):
           self.turtles.extend(other.turtles)
           return Town(*self.turtles)
       else:
           return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            multiple = list(itertools.chain.from_iterable(itertools.repeat(self.turtles, other)))
            return Town(*multiple)
        else:
            return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, int):
            return Town.__mul__(self, other)
        else:
            return NotImplemented

    def __imul__(self, other):
        if isinstance(other, int):
            multiple=list(itertools.chain.from_iterable(itertools.repeat(self.turtles, other)))
            return Town(*multiple)
        else:
            return NotImplemented
        

    def __getitem__(self, item):
        return self.data[item]

    if __name__ == "__main__":
        """ Die folgenden Aufrufe sollen funktionieren """

    # Create MyTurtle instances
    t1 = House(30, 3)
    t2 = House(20, 2)
    t3 = Tree(10, 2)

    # Draw House t1
    t1()
    turtle.setpos(50, 0)
    # Draw House t2
    t2()
    turtle.setpos(100, 0)
    # Draw Tree t3
    t3()
    turtle.setpos(150, 0)


    #town1 = t3 + (t2 + t3) * 2 + t1

    town1 = [t3, t2, t3, t2, t3, t1]
    # Draw town1
    pos = 200
    for element in town1:
        element()
    turtle.setpos(pos, 0)
    pos += 50

    #town1()

    turtle.penup()
    turtle.setpos(0, -150)
    turtle.pendown()

    # Initiate Town instance
    #town2 = Town(t2)
    town2 *= 2
    town3 = Town(t1, 3 * t3) + town2
    town3 += t3

    # Draw town3
    town3()

    turtle.penup()
    turtle.setpos(0, 150)
    turtle.pendown()

    town4 = Tree(5, 2) + Tree(10, 1) + House(10, 2) + 2 * House(10, 1)
    town4 += Tree(7, 3)
    # Draw town4
    town4()

    turtle.dot()
    turtle.done()
