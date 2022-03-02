from threading import Thread
import sys
sys.path.append("../Code/Server/")

from servo import *


class ServoThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.servo = Servo()
        self.current_degree_0, self.current_degree_1 = 90, 90
        self.update()

    def run(self):
        pass

    def update(self):
        self.servo.setServoPwm('0', self.current_degree_0)
        self.servo.setServoPwm('1', self.current_degree_1)

    def move(self, in_val):
        if in_val == "H":
            self.current_degree_0 = max(self.current_degree_0 - 10, 0)
        elif in_val == "J":
            self.current_degree_0 = min(self.current_degree_0 + 10, 180)
        elif in_val == "K":
            self.current_degree_1 = max(self.current_degree_1 - 10, 0)
        elif in_val == "L":
            self.current_degree_1 = min(self.current_degree_1 + 10, 180)
        self.update()