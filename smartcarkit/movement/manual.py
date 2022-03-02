from threading import Thread
import sys
sys.path.append("../Code/Server/")

from Motor import *

class ManualMovement(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.PWM = Motor()
        # D: rotate clockwise
        # A: rotate counterclockwise
        # W: proceed forward
        # S: proceed backward
        # X: stop current operation
        # V: stop everytihing

    def run(self):
        pass

    def move(self, in_val):
        if in_val == "W":
            self.forward()
        elif in_val == "S":
            self.backward()
        elif in_val == "A":
            self.rotate_left()
        elif in_val == "D":
            self.rotate_right()
        else:
            self.stop()

    def forward(self):
        self.PWM.setMotorModel(1000, 1000, 1000, 1000)

    def backward(self):
        self.PWM.setMotorModel(-1000, -1000, -1000, -1000)

    def rotate_left(self):
        self.PWM.setMotorModel(-1000, -1000, 1500, 1500)

    def rotate_right(self):
        self.PWM.setMotorModel(1500, 1500, -1000, -1000)

    def stop(self):
        self.PWM.setMotorModel(0, 0, 0, 0)  # Stop
