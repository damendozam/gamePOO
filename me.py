import turtle

class Me(turtle.Turtle):
    element=turtle.Turtle()
    def __init__(self,color,form,position):
        self.element.penup()
        self.element.shape(form)
        self.element.color(color)
        self.element.goto(position[0],position[1])

