import time

class Game:
    def __init__(self):
        self.on = True
        self.tick_speed = 0.005
    def tick(self, screen):
        screen.update()
        time.sleep(self.tick_speed)