from graphics import *
import random
from time import sleep
win = GraphWin("Creare Sistemas",1366, 768, autoflush=False)
red, green, blue = random.randint(0,255), random.randint(0,255), random.randint(0,255)
box = Rectangle(Point(0,0), Point(500,500))
box.setFill(color_rgb(red, green, blue))
box.draw(win)
logText = Text(Point(250, 200), "Número de Madeiras Cortadas:")
logText.setFill(color_rgb(255, 255, 255))
logText.setSize(20)
logText.draw(win)
cont = 0
random.seed()
while not win.isClosed():
    logNumbers = Text(Point(250, 250), f"{cont}")
    logNumbers.setFill(color_rgb(255, 255, 255))
    logNumbers.setSize(30)
    logNumbers.draw(win)
    cont += random.randint(5,15)
    update(60)
    logNumbers.undraw()
    sleep(1)
    
win.close()