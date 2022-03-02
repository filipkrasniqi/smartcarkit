import sys
sys.path.append("../Code/Server/")

from Motor import *

if __name__ == "__main__":

    PWM = Motor()
    # D: rotate clockwise
    # A: rotate counterclockwise
    # W: proceed forward
    # S: proceed backward
    # X: stop current operation
    # V: stop everytihing

    # TODO inizio con (0,0).

    in_val = ""
    while in_val != "V":
        # while in_val != "X":
        in_val = input("Gimme input (WASD + X + V)").upper()
        if in_val == "W":
            PWM.setMotorModel(1000, 1000, 1000, 1000)  # Forward
        elif in_val == "S":
            PWM.setMotorModel(-1000, -1000, -1000, -1000)  # Backward
        elif in_val == "A":
            PWM.setMotorModel(-1000, -1000, 1500, 1500)  # Left
        elif in_val == "D":
            PWM.setMotorModel(1500, 1500, -1000, -1000)  # Right
        else:
            PWM.setMotorModel(0, 0, 0, 0)  # Stop

    print("End of program")