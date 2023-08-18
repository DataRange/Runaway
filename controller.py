import pygame.joystick as pgjoy

class XboxController:

    def __init__(self, port):

        pgjoy.init()

        self.joy = pgjoy.Joystick(port)
        
    def getLeftX(self) -> float: return self.joy.get_axis(0)

    def getLeftY(self) -> float: return self.joy.get_axis(1)

    def getLeftTrigger(self) -> float: return self.joy.get_axis(2)

    def getRightX(self) -> float: return self.joy.get_axis(3)

    def getRightY(self) -> float: return self.joy.get_axis(4)

    def getRightTrigger(self) -> float: return self.joy.get_axis(5)

    def getButtonA(self) -> bool: return self.joy.get_button(0)

    def getButtonB(self) -> bool: return self.joy.get_button(1)

    def getButtonX(self) -> bool: return self.joy.get_button(2)

    def getButtonY(self) -> bool: return self.joy.get_button(3)

    def getLeftBumper(self) -> bool: return self.joy.get_button(4)

    def getRightBumper(self) -> bool: return self.joy.get_button(5)

    def getLeftPress(self) -> bool: return self.joy.get_button(8)

    def getRightPress(self) -> bool: return self.joy.get_button(9)

    def getHatX(self) -> int: return self.joy.get_hat(0)

    def getHatY(self) -> int: return self.joy.get_hat(1)