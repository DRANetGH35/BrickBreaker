import turtle


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
        self.position = position
        self.velocity = velocity
        self.setheading(orientation + 90)
        self.shape("circle")
        self.color("white")
        self.penup()

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
