import Ders08.Pisti.Kart as Kart
import random

class Deste():
    def __init__(self):
        self.kart_liste = []
        for f in Kart.FACES:
            for s in Kart.SUITES:
                self.kart_liste.append(Kart.Kart(s, f))
        random.shuffle(self.kart_liste)

    def rastgele_kart(self):
        if len(self.kart_liste) > 0:
            bir_kart = random.choice(self.kart_liste)
            self.kart_liste.remove(bir_kart)
            return bir_kart

    def is_empty(self):
        return len(self.kart_liste) == 0

    def __str__(self):
        s = ""
        for k in self.kart_liste:
            s += str(k)+"\n"

        return s


