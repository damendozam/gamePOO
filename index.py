import turtle
from me import Me
from enemy import Enemy

import time

window=turtle.Screen()
window.bgcolor('black')
me=Me(turtle.Turtle())
me.begin()
enemy=[]
for i in range(5):
    newEnemy=Enemy(turtle.Turtle())
    newEnemy.begin()
    enemy.append(newEnemy)


window.mainloop()

