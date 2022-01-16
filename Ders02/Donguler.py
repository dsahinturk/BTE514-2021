import random

def basit_dongu():
    print("******************* Basit bir döngü ******************")
    count = 1
    while count<5:
        count = count + 1
        print(count, end=" ")
    else:
        print()
    print("******************* Basit bir döngü ******************\n")



def not_ortalama():
    print("******************* Not ortalaması ******************")

    # ogr_say = int(input("Kac ogrenci notu gireceginizi yaziniz "))
    # print(ogr_say," adet ogrenci notu giriniz")

    print("Lutfen notları giriniz. Durmak için -1 giriniz")
    count = 1
    toplam = 0
    ogr_not = 0

    while ogr_not != -1:
        ogr_not = int(input(str(count) + ". ogrenci notunu giriniz "))
        if ogr_not == -1:
            break
        elif ogr_not < 0:
            print("Lutfen negatif not girmeyiniz")
            continue
        toplam += ogr_not
        count += 1

    print("Ortalama", toplam / (count - 1))
    print("******************* Not ortalaması ******************\n")


def sayi_oyunu():
    print("******************* Sayı tahmin oyunu ******************")
    tutulan_sayi = random.randint(1, 100)

    print("0 ile 100 arası bir sayı tuttum")
    tahmin_say = 0
    while True:
        tahmin = int(input("Tahmin ettiğiniz sayı? "))
        tahmin_say += 1

        if tahmin > tutulan_sayi:
            print("Daha küçük bir sayi deneyin")
        elif tahmin < tutulan_sayi:
            print("Daha büyük bir sayi deneyin")
        else:
            print("Tebrikler",tahmin_say,"kerede bildiniz")
            break
    print("******************* Sayı tahmin oyunu ******************\n")

