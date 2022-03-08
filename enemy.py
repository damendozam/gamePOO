import turtle
from gamer import Gamer

class Enemy(Gamer):
    element=turtle.Turtle()
    position=[]
    def begin(self):
        self.element.penup()
        self.element.shape('square')
        self.element.color('red')
        self.element.goto(self.position[0],self.position[1])

