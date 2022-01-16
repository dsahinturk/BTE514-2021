from Ders08.Pisti.Kart import Kart
from Ders08.Pisti.Deste import Deste
from Ders08.Pisti import Oyuncular

def oyun():
    bir_deste = Deste()
    bilg = Oyuncular.Bilgisayar()
    oyuncu = Oyuncular.Oyuncu()

    yer = []
    for i in range(4):
        yer.append(bir_deste.rastgele_kart())

    for kart in yer:
        print(kart, end=" ")

    while not bir_deste.is_empty():
        bilg.el_cek(bir_deste)
        oyuncu.el_cek(bir_deste)
        for i in range(4):
            yer.append(bilg.oyna())
            print("Bilgisayar oynadı:", yer[-1])
            if len(yer)>2 and yer[-1].face == yer[-2].face:
                print("PİSTİ!!!!!")
                bilg.puan_aktar(yer)



            yer.append(oyuncu.oyna())
            print("Oyuncu oynadı:", yer[-1])
            if len(yer)>2 and yer[-1].face == yer[-2].face:
                print("PİSTİ!!!!!")
                oyuncu.puan_aktar(yer)