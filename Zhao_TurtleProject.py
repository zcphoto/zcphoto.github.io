import turtle
import random



turtle.bgcolor("black")

wn = turtle.Screen()
dan = turtle.Turtle()
dan.shape('arrow')
dan.speed(0)
turtle.colormode(255)


r = 0
g = 0
b = 0

def square():
    for i in range (4):
        dan.forward(100)
        dan.left(90)

def triangle():
    for i in range (3):
        dan.forward(100)
        dan.left (120)

def pentagon():
    for i in range (5):
        dan.forward(100)
        dan.left(72)

def hexagon():
    for i in range (6):
        dan.forward(100)
        dan.left(60)

def nonagon():
    for i in range (9):
        dan.forward(100)
        dan.left(40)

def decagon():
    for i in range (10):
        dan.forward(100)
        dan.left(36)

def csquare(t, length):
   for i in range(4):
       t.forward(length)
       t.left(90)

def anyshape(q,l):
   for i in range(q):
      r = random.randint(0,255)
      g = random.randint(0,255)
      b = random.randint(0,255)
      dan.forward(l)
      dan.stamp()
      dan.right(360/q)
      dan.pencolor(r,g,b)
      

def concentrics(x):
   sizechange = 1
   for i in range(x):
      r = random.randint(0,255)
      g = random.randint(0,255)
      b = random.randint(0,255)
      dan.pencolor(r,g,b)
      csquare(dan, sizechange)
      sizechange += 20
      dan.penup()
      dan.backward(10)
      dan.right(90)
      dan.forward(10)
      dan.left(90)
      dan.pendown()

def polycorner(p,z):
   sizechange = 1
   for i in range (p):
      r = random.randint(0,255)
      g = random.randint(0,255)
      b = random.randint(0,255)
      dan.pencolor(r,g,b)
      anyshape(z, sizechange)
      sizechange +=20


polycorner (7,6)
concentrics (10)
anyshape (9,18)




   

