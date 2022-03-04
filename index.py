import turtle
from me import Me
from enemy import Enemy

import time


me=Me('blue','square',[40,40])
enemyAux=Enemy('red','square')
enemy=[]
for i in range(5):
    enemyAux.position(50*i,50*i)
    enemy.append(enemyAux)
    time.sleep(1)

window=turtle.Screen()
window.bgcolor('black')
window.mainloop()

