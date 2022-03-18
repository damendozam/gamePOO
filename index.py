import turtle
import math
import time

def circle_function(radians, radius):
    
    """
    Calculate the coordinates of the
    edge of the circle at the given angle.
    """

    return {"x": math.cos(radians) * radius,
            "y": math.sin(radians) * radius}


window=turtle.Screen()
window.bgcolor('black')


sun= turtle.Turtle()
sun.shape('circle')
sun.penup()
sun.color('yellow')
sun.goto(0,0)

earth=turtle.Turtle()
earth.shape('circle')
earth.penup()
earth.color('blue')

mars=turtle.Turtle()
mars.shape('circle')
mars.penup()
mars.color('red')


sat1=turtle.Turtle()
sat1.shape('circle')
sat1.penup()
sat1.color('white')
sat2=turtle.Turtle()
sat2.shape('circle')
sat2.penup()
sat2.color('white')


for degrees in range(36000):
    posEarth = circle_function(math.radians(degrees), 100)
    posMars = circle_function(math.radians(degrees)*math.sqrt((1/1.52)**3), 152)
    posSat1 = circle_function(math.radians(degrees-60), 100)
    posSat2 = circle_function(math.radians(degrees+60), 100)
    earth.goto(posEarth["x"], posEarth["y"])
    mars.goto(posMars["x"], posMars["y"])
    sat1.goto(posSat1["x"], posSat1["y"])
    sat2.goto(posSat2["x"], posSat2["y"])
    time.sleep(0.002)
    




window.mainloop()