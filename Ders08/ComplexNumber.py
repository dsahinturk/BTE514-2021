class ComplexNumber:
    def __init__(self, a, b):
        self.reel = a
        self.img = b

    def print(self):
        print(str(self.reel), str(self.img) + "i")

    def __str__(self):
        return str(self.reel) + " " + str(self.img) + "i"

    def __add__(self, other):
        return ComplexNumber(self.reel + other.reel, self.img + other.img)

