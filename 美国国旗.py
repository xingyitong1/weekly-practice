import turtle as t
import math
#画长方形
def rectangle(x0,y0):
    t.pu()
    t.goto(x0,y0)
    t.pd()
    for i in range(2):
        t.forward(abs(2*x0))
        t.right(90)
        t.forward(abs(2*y0))
        t.right(90)
#画条纹
def drawline(x0,y0):
    y = y0
    for i in range(13):
        t.pu()
        t.goto(-190,y)
        t.pd()
        if i % 2 ==1:
            t.begin_fill()
            t.fillcolor("white")
            t.forward(abs(2*x0))
            t.right(90)
            t.forward(abs(2*y0)/13)
            t.right(90)
            t.forward(abs(2*x0))
            t.right(90)
            t.forward(abs(2*y0)/13)
            t.end_fill()
        else :
            t.begin_fill()
            t.fillcolor("red")
            t.forward(abs(2*x0))
            t.right(90)
            t.forward(abs(2*y0)/13)
            t.right(90)
            t.forward(abs(2*x0))
            t.right(90)
            t.forward(abs(2*y0)/13)
            t.end_fill()
        y-=abs(2*y0)/13
        t.setheading(0)
#画蓝色区域
def bluerectangle(x0,y0):
    t.pu()
    t.goto(x0,y0)
    for i in range(2):
        t.pd()
        t.begin_fill()
        t.fillcolor("blue")
        t.forward(2*abs(2*x0)/5)
        t.right(90)
        t.forward(7*abs(2*y0)/13)
        t.right(90)
        t.end_fill()
#画白色五角星
def whitestar(x,y,x0,y0):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.setheading(180)
    t.backward(0.0616/1.9*2*x0/2)
    t.pd()
    t.begin_fill()
    t.fillcolor("white")
    t.pencolor("white")
    for i in range(5):
        t.forward(0.0616/1.9*2*x0)
        t.right(144)
    t.end_fill()
    t.pu()
#画五十颗白色五角星
def fifty_whitestars(x0,y0):
    for i in range(9):
        if i%2 == 0:
            x = x0+(abs(2*x0)/30)
            y = y0-(i+1)*(abs(2*y0)*7/130)
            for j in range(6):
                whitestar(x,y,x0,y0)
                x+=abs(2*x0)/15
        else:
            x = x0 +2*(abs(2*x0)/30)
            y = y0-(i+1)*(abs(2*y0)*7/130)
            for j in range(5):
                whitestar(x,y,x0,y0)
                x+=abs(2*x0)/15


#主程序
t.speed(10)
rectangle(-190,100)
drawline(-190,100)
bluerectangle(-190,100)
fifty_whitestars(-190,100)




        
            
            
            
    
        
