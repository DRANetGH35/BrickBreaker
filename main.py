import turtle
from Objects import ObjectManager, Ball, Line
from Game import Game
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

object_manager = ObjectManager()

object_manager.add_object(Ball())
line = Line((0, 0), (100, 100))

game = Game()

while game.on:
    for obj in object_manager.get_objects():
        obj.forward(obj.velocity)
    game.tick(screen)


turtle.mainloop()