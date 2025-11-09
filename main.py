import turtle
from Objects import ObjectManager, Ball, Line
from Game import Game
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

object_manager = ObjectManager()
ball = Ball()
ball2 = Ball(position=(0, 30), velocity=0)
object_manager.add_object(ball)
object_manager.add_object(ball2)



game = Game()

while game.on:
    for obj in object_manager.get_objects():
        obj.forward(obj.velocity)
    if ball.detect_collision(ball2):
        ball.color("green")
    game.tick(screen)


turtle.mainloop()