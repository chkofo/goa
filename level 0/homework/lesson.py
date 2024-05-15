from turtle import *


#we want to paint a house

#step 1:  draw a square
speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end od square



forward(70)
color('yellow')
left(90)
forward(120)   #height of the floor
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()



penup()
goto(20,140)
pendown()

color('red')
begin_fill()
width(5)
left(120)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()

penup()
goto(180,140)
pendown()   

color('red')
begin_fill()
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)    
right(90)
forward(40)
end_fill()

exitonclick()
