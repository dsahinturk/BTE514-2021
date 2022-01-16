import random
def sayi_tahmin_oyunu():
    print("******************* Sayı tahmin oyunu 2 ******************")
    print("Lütfen 1 ile 100 arasında bir sayı tutun")

    tahmin_say = 0
    alt_sinir = 1
    ust_sinir = 100

    bilg_tahmin = random.randint(alt_sinir, ust_sinir)
    tahmin_say = 1

    while True:
        print("Tahminim", bilg_tahmin)

        durum = input("Tahminim dogru mu? (Y)ukarı, (A)şağı, (E)vet ")

        if durum == "Y" or durum == "A" or durum == "E":
            if durum == "Y":
                alt_sinir = bilg_tahmin + 1
            elif durum == "A":
                ust_sinir = bilg_tahmin - 1
            elif durum == "E":
                print(tahmin_say, "kerede bildim")
                break
            bilg_tahmin = random.randint(alt_sinir, ust_sinir)
            tahmin_say += 1
        else:
            print("Y A E değerlerinden birini giriniz")
            continue
    print("******************* Sayı tahmin oyunu 2 ******************\n")

def for_piramitler():
    print("******************* For donguleri ve piramitler ******************")

    for var in "Tolga":
        print(var, end="-")

    print()

    for i in range(5):
        print(i, end=" ")

    print()

    for i in range(4, 12):
        print(i, end=" ")

    print()

    for i in range(6, 40, 7):
        print(i, end=" ")


    print()

    for i in range(40, 2, -5):
        print(i, end=" ")

    print()

    count = 1
    while count < 5:
        for i in range(9):
            print(i*count, end=" ")
        print()
        count += 1
    print("******************* For donguleri ve piramitler ******************\n")

def ic_ice_for():
    print("******************* İç içe döngüler ******************")

    yukseklik = 5

    for i in range(yukseklik):
        for j in range(i+1):
            print('*', end="")
        print()

    for i in range(yukseklik):
        for j in range(yukseklik-i):
            print('*', end="")
        print()

    for i in range(yukseklik):
        for j in range(yukseklik-i-1):
            print('.', end="")
        for j in range(i+1):
            print('*', end="")
        print()

    print("******************* İç içe döngüler ******************\n")
