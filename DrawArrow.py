import turtle as t
import random


#画x，y轴函数
def zuobiaozhou(x0,y0):
#画x轴
    t.pu()
    t.goto(x0-80,y0)
    t.pd()
    t.goto(x0+80,y0)
#画y轴
    t.pu()
    t.goto(x0,y0-80)
    t.pd()
    t.goto(x0,y0+80)


def drawarrow(direction):
    t.setheading(direction-135)
    t.forward(10)
    t.backward(10)
    t.setheading(direction+135)
    t.forward(10)
    t.backward(10)


def drawline(x1,y1,x0,y0,direction,mycolor,length,size):
    t.pu()
    t.goto(x1,y1)
    t.pd()
    t.setheading(direction)
    t.pencolor(mycolor)
    t.pensize(size)
    t.forward(length)
    drawarrow(direction)


zuobiaozhou(0,0)


for i in range(11):
    x1 = random.randint(-80,80)
    y1 = random.randint(-80,80)
    size = random.randint(1,4)
    color = random.randint(1,4)
    if(color == 1):
        mycolor = "red"
    if(color == 2):
        mycolor = "blue"
    if(color == 3):
        mycolor = "green"
    if(color == 4):
        mycolor = "yellow"
    direction = random.randint(0,360)
    length = random.randint(50,100)
    drawline(x1,y1,0,0,direction,mycolor,length,size)





    
