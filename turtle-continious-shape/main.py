from turtle import Turtle,Screen
from colorPicker import ColorPicker
from increment import Increment
from colorsData import colorsList

tim=Turtle()
tim.shape("turtle")

screen=Screen()
sides=3


for i in colorsList:
    tim.color(i,"cyan")
    increment=Increment(tim,sides)
    increment.increasing_sides()
    
    sides+=1



screen.exitonclick()
