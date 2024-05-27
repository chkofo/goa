import turtle
from turtle import*
speed(5000)
width(7)
#ჩვენ გვინდა,რომ დავხატოთ სასახლე, დედოფალი, მეფე და GOA-ს აკადემიის დროშა

# პირველი ნაბიჯი: ავაშენოთ სასახლე

penup()
goto(-450,-350)
pendown()

forward(500)
left(90)
forward(200)
left(90)
forward(500)
left(90)
forward(200)

penup()
goto(-200,-350)
pendown()

left(180)
forward(75)
left(90)
forward(50)
left(90)
forward(75)

penup()
goto(-200,-275)
pendown()

left(90)
forward(50)
right(90)
forward(75)

penup()
goto(-250,-150)
pendown()

left(180)
forward(175)
right(90)
forward(100)
right(90)
forward(175)

penup()
goto(-180,-100)
pendown()

left(180)
forward(75)
left(90)
forward(50)
left(90)
forward(75)
left(90)
forward(50)

penup()
goto(-250,25)
pendown()

left(75)
forward(170)
right(145)
forward(170)

penup()
goto(-450,-350)
pendown()

right(110)
forward(100)
right(90)
forward(375)
right(90)
forward(100)
right(90)
forward(175)

penup()
goto(-450,25)
pendown()

right(160)
forward(160)
right(216)
forward(160)

penup()
goto(-525,-25)
pendown()

right(344)
forward(75)
left(90)
forward(50)
left(90)
forward(75)
left(90)
forward(50)

penup()
goto(50,-350)
pendown()

right(180)
forward(100)
left(90)
forward(375)
left(90)
forward(100)
left(90)
forward(175)

penup()
goto(120,-30)
pendown()

forward(75)
right(90)
forward(50)
right(90)
forward(75)
right(90)
forward(50)

penup()
goto(50,25)
pendown()

left(75)
forward(175)
right(147)
forward(175)

#მეორე ნაბიჯი : სასხლეს დავადგათ GOA-ს დროშა
penup()
goto(-206,183)
pendown()

right(198)
forward(170)
left(90)
forward(200)
left(90)
forward(100)
left(90)
forward(200) 

penup()
goto(-345,330)
pendown()

left(180)
forward(40) 
left(90)
forward(55)
left(90)
forward(40)
left(90)
forward(28)
left(90)
forward(20)


circlee=turtle.Turtle()
circlee.penup()
circlee.goto(-300,275)
circlee.pendown()
circlee.width(7)
circlee.speed(5000)
circlee.circle(28)

penup()
goto(-270,275)
pendown()

right(115)
forward(60)
right(135)
forward(60)

penup()
goto(-258,295)
pendown()

left(70)
forward(30)

#ნაბიჯი მესამე: დავხატოთ მეფე და დედოფალი
king=turtle.Turtle()
king.penup()
king.goto(220,-200)
king.pendown()
king.width(7)
king.circle(25)
king.right(90)
king.forward(100)
king.right(25)
king.forward(50)

king.penup()
king.goto(220,-300)
king.pendown()

king.left(50)
king.forward(50)

king.penup()
king.goto(220,-230)
king.pendown()

king.right(45)
king.forward(50)

king.penup()
king.goto(220,-230)
king.pendown()

king.left(45)
king.forward(50)

king.penup()
king.goto(205,-158)
king.pendown()

king.right(220)
king.forward(30)

king.right(150)
king.forward(30)

king.left(140)
king.forward(30)
king.right(135)
king.forward(30)

queen=turtle.Turtle()
queen.penup()
queen.goto(330,-200)
queen.pendown()
queen.width(7)
queen.circle(25)
queen.right(90)
queen.forward(100)

queen.penup()
queen.goto(330,-300)
queen.pendown()

queen.right(25)
queen.forward(50)

queen.penup()
queen.goto(330,-300)
queen.pendown()

queen.left(50)
queen.forward(50)

queen.penup()
queen.goto(330,-230)
queen.pendown()

queen.right(40)
queen.forward(50)

queen.penup()
queen.goto(330,-230)
queen.pendown()

queen.left(30)
queen.forward(50)

turtle.done()
exitonclick()