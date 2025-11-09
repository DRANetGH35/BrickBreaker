import time

class Game:
    def __init__(self):
        self.on = True
        self.tick_speed = 1
    def tick(self, screen):
        screen.update()
        time.sleep(self.tick_speed)