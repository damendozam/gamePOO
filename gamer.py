import turtle
from random import random

class Gamer(object):
    element=turtle.Turtle()
    position=[]
    def __init__(self,element):
        self.element=element
        positionBegin()
    def positionBegin(self):
        self.element.goto(500*random()-250,500*random()-250)

    
    

