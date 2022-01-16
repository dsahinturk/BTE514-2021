import random

class Bilgisayar():
    def __init__(self):
        self.el = []
        self.puan = []

    def el_cek(self, bir_deste):
        for i in range(4):
            self.el.append(bir_deste.rastgele_kart())

    def oyna(self):
        bir_kart = random.choice(self.el)
        self.el.remove(bir_kart)
        return bir_kart

    def puan_aktar(self, yer):
        self.puan += yer
        yer.clear()

class Oyuncu():
    def __init__(self):
        self.el = []
        self.puan = []

    def el_cek(self, bir_deste):
        for i in range(4):
            self.el.append(bir_deste.rastgele_kart())

    def oyna(self):
        for i in range(len(self.el)):
            print("[{0}] {1}".format(i+1, self.el[i]), end=" ")
        else:
            print()

        if len(self.el)>1:
            print("Lutfen [1-{0}] bir kart seçiniz".format(len(self.el)))
            secim = int(input())
        else:
            secim = 1
        bir_kart = self.el[secim-1]
        self.el.remove(bir_kart)
        return bir_kart


    def puan_aktar(self, yer):
        self.puan += yer
        yer.clear()