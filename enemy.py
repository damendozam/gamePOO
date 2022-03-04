import turtle

class Enemy(turtle.Turtle):
    element=turtle.Turtle()
    def __init__(self,color,form,position):
        self.element.penup()
        self.element.shape(form)
        self.element.color(color)
        self.element.goto(position[0],position[1])
    def __init__(self,color,form):
        self.element.penup()
        self.element.shape(form)
        self.element.color(color)
    def position(self,x,y):
        self.element.goto(x,y)

