SUITES = ["KARO","SINEK","MACA","KUPA"]
FACES = ["AS","2","3","4","5","6","7","8","9","10", "VALE", "KIZ", "PAPAZ"]

class Kart():
    def __init__(self, suit="SINEK", face="PAPAZ"):
        if suit in SUITES:
            self.suit = suit
        else:
            self.suit = "KARO"
        if face in FACES:
            self.face = face
        else:
            self.face = "AS"
        self.flipped = True



    def __str__(self):
        if not self.flipped:
            return "*****"
        return self.suit +" "+self.face