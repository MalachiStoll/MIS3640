import turtle

alex = turtle.Turtle()

#print(alex)

for i in range(4):
    alex.fd(100)
    alex.lt(90)

#square(alex, 250)

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

#square(alex, 50)


def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

#polygon(alex,10,8)

import math

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 10
    length = circumference / n 
    polygon(t,length, n )

#circle(alex, 80)

def arc(t, r, angle):
    circumference = 2 * math.pi * r * angle /360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n

    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

arc(alex, 100, 100) 

turtle.mainloop()