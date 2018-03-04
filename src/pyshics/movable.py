import math
import asyncio
class Movable():
    posx = 0.0
    posy = 0.0
    max_speed = 0.0
    speed = 0.0
    speed_ramp_ms = 100
    delta_speed = 0.0
    def __init__(self):
        delta_speed = max_speed / speed_ramp_ms
    def async rampSpeed():
        speed = 0.0
        while True:
            speed += delta_speed
            if(speed >= max_speed):
                break
            await asyncio.sleep(1)
    def move(angle,dt):
        self.posx += self.speed * math.cos(angle) * dt
        self.posy += self.speed * math.sin(angle) * dt
