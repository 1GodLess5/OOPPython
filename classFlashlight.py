# simple class Flashlight

class Flashlight:
    def __init__(self, color, isOn):
        self.color = color
        self.isOn = isOn

    def turnOn(self):
        self.isOn = True

    def turnOff(self):
        self.isOn = False
