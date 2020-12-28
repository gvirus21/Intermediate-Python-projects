from turtle import Turtle

class Increment:
    def __init__(self,turtle,sides):
        self.sides=sides
        self.turtle=turtle
    def increasing_sides(self):
        for i in range(self.sides):
            self.turtle.forward(100)
            self.turtle.right(360/self.sides)
            

            



            