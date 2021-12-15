import turtle as t

t.speed(10)
t.hideturtle()


#画红色长方形
def rectangle():
    t.pu()
    t.goto(-150,100)
    t.pd()
    t.pencolor("red")
    t.begin_fill()
    t.fillcolor("red")
    t.forward(300)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(300)
    t.right(90)
    t.forward(200)
    t.end_fill()

#画五角星
def drawstar(size,x,y,seth=0):
    t.goto(x,y)
    t.setheading(seth)
    t.backward(size*1.1756/2)
    t.pd()
    t.begin_fill()
    t.fillcolor("yellow")
    t.pencolor("yellow")
    for i in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()
    t.pu()

#画国旗
def drawflag():
    rectangle()
    drawstar(51,-100,50)
    drawstar(20,-50,80,30)
    drawstar(20,-30,60,-30)
    drawstar(20,-30,30)
    drawstar(20,-50,10,30)


drawflag()

    
    
    
    
    
