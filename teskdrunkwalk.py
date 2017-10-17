def drunkard_walk(x, y, n):
    import random
    import turtle
    #Walk increased by a scale of 30 so that it can be seen on the console. Full screen for full picture.
    draw=turtle.Turtle()
    scale = 30
    t=turtle
    oldx=x
    oldy=y
    draw.penup()
    draw.speed(1)
    directions = ['l','r','u','d']
    draw.goto(oldx*scale,oldy*scale)
    draw.pendown()
    for i in range(n):
        direction = random.choice(directions)
        if direction == 'l':
            x=x-1
            print('The drunkard goes left')
        if direction == 'r':
            x=x+1
            print('The drunkard goes right')
        if direction =='u':
            y=y+1
            print('The drunkard goes up')
        if direction =='d':
            y=y-1
            print('The drunkard goes down')
        draw.goto(x*scale,y*scale)
    distance = ((x-oldx)**2 + (y-oldy)**2)**(1/2)
    print("The drunkard started from (%d,%d) and ended on (%d,%d)." % (oldx, oldy, x, y))
    print("After", n, "intersections, he's {:.2f} blocks from where he started.".format(distance))
    turtle.mainloop()

#when entering in coordinates, use a smaller number <100 recommended
drunkard_walk(2,3,6)