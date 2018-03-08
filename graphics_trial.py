from graphics import *

mywindow = GraphWin(width = 500, height = 300)

mywindow.setCoords(-20,-20,120,80)

mySquare = Rectangle(Point(0,0), Point(100,60))

mySquare.draw(mywindow)

mywindow.getMouse()
