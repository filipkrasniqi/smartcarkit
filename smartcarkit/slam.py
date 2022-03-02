import sys

from smartcarkit.movement.manual import ManualMovement
from smartcarkit.sensor.ultrasonic import DistanceSensor

sys.path.append("../Code/Server/")

from Ultrasonic import *

class SLAM:
    def __init__(self):
        self.movement = ManualMovement()
        self.movement.run()
        self.distance_sensor = DistanceSensor(movement=self.movement)
        self.distance_sensor.run()

    def run(self):
        in_val = ""
        while in_val != "V":
            # while in_val != "X":
            in_val = input("Gimme input (WASD + X + V)").upper()
            self.movement.move(in_val)