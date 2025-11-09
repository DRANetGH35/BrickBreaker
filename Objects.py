import turtle
import math

class ObjectManager:
    def __init__(self):
        self.objects = []
    def add_object(self, obj):
        self.objects.append(obj)
    def remove_object(self, obj):
        self.objects.remove(obj)
    def get_objects(self):
        return self.objects

class Ball(turtle.Turtle):
    def __init__(self, position=(0, 0), velocity=1, orientation=0):
        super().__init__()
        self.radius = self.shapesize()[0] * 22.5
        self.goto(position)
        self.velocity = velocity
        self.setheading(orientation + 90)
        self.shape("circle")
        self.color("white")
        self.penup()
    def detect_collision(self, other):
        x_distance = abs(self.xcor() - other.xcor())
        y_distance = abs(self.ycor() - other.ycor())
        if type(other) == Ball:
            distance = math.sqrt(x_distance**2 + y_distance**2)
            if distance <= self.radius/2 + other.radius/2:
                self.color("red")

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        drawer = turtle.Turtle()
        drawer.color("white")
        drawer.hideturtle()
        drawer.penup()
        drawer.goto(self.start)
        drawer.pendown()
        drawer.goto(self.end)
        drawer.penup()
