import sys
from threading import Thread
from time import sleep

sys.path.append("movement/")
from manual import ManualMovement

sys.path.append("../Code/Server/")

from Ultrasonic import *

class DistanceSensor(Thread):
    def __init__(self, movement: ManualMovement = None):
        Thread.__init__(self)
        self.ultrasonic = Ultrasonic()
        self.running = True
        self.last_read = -1
        self.movement = movement

    def run(self):
        while self.running:
            self.last_read = self.ultrasonic.get_distance()
            print("Last value {}".format(self.last_read))
            if self.last_read < 50 and self.movement is not None:
                self.movement.stop()
            sleep(1)