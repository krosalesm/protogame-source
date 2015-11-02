import imports


class Weapons:

    def __init__(self):
        self.chargeMax = 10
        self.bullets = 0
        self.reloadTime = 1.2
        self.acurrancy = 1/10
        self.fireSpeed = 1
        self.distance = 10
        self.img = None
        self.name = ""
        self.bulletsMax = 10
        self.bulletsTotal = 1

    def reload(self):
        print("Reload")

    def shoot(self):
        print("shoot")
