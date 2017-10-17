import turtle
import random

def drunkards_walk_turtle (n):
    x = 0
    y = 0
    t = turtle.Turtle()
    direction = (1,2,3,4)

    for i in range(n):
        walk = random.choice(direction) 

        if walk == 1:
            t.fd(25)
            y += 1
        if walk == 2:
            t.rt(90)
            t.fd(25)
            x += 1
        if walk == 3:
            t.lt(-25)
            y -= 1
        if walk == 4:
           t.lt(270)
           t.fd(25)
           x -= 1

    distance = (x+y)
    print("The Distance between start and end is %d Blocks " %(distance))
    turtle.mainloop()
    
drunkards_walk_turtle(6)

