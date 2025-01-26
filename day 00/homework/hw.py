from turtle import *

#we want paint a house

#step 1:  draw a square

speed(30)
width(6)
color("black")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("brown")
begin_fill()
left(90)
forward(120)   #heigt of the door

right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("grey")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(170, 170)
pendown()

color("lightblue")
begin_fill()
right(60)
forward(35)
left(90)
forward(35)
left(90)
forward(35)
left(90)
forward(35)
end_fill()

penup()
goto(200, 200)
pendown()

penup()
goto(30, 170)
pendown()

color("lightblue")
begin_fill()
right(90)
forward(35)
right(90)
forward(35)
right(90)
forward(35)
right(90)
forward(35)
end_fill()

exitonclick()