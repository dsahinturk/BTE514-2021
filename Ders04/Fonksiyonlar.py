def bmi_hesapla(kilo, boy):
    boy_kare = boy * boy
    bmi = kilo / boy_kare
    return bmi


def bmi_yazdir(kilo, boy=0):
    if kilo <= 0:
        print("Kilo degeri hatali")
        return
    print(bmi_hesapla(kilo, boy))


def fonksiyon_tanimlama():
    print("******************* Fonksiyonlar ******************")
    weight = 0
    height = 1.8
    bmi_yazdir(boy=height, kilo=weight)
    print(bmi_hesapla(weight, height))
    print("******************* Fonksiyonlar ******************\n")


a = 10
b = 5

def swap(x, y):
    temp = y
    y = x
    x = temp

def degis_tokus():
    print("******************* Etki alanı ve global ******************")

    global a
    global b

    a, b = b, a

    swap(a, b)

    print(a, b)
    print("******************* Etki alanı ve global ******************\n")

def ebob_euclid(a, b):

    while True:
        buyuk = max(a, b)
        kucuk = min(a, b)

        kalan = buyuk % kucuk
        if kalan == 1:
            return 1
        if kalan == 0:
            return kucuk

        a = kalan
        b = kucuk

def euclid_alg():
    print("******************* Öklid ile ebob ******************")
    print("184 ile 245'in ebobu:", ebob_euclid(184, 245))
    print("******************* Öklid ile ebob ******************\n")

def collatz_seq(num, to_print=False):
    if to_print:
        print(num, end=" ")
    count = 0
    while num != 1:
        count = count +1
        if num % 2 == 0:
            num = num // 2
        else:
            num = num*3+1
        if to_print:
            print(num, end=" ")

    return count

def find_largest_collatz(limit):
    print("******************* En buyuk Collatz sayısı ******************")
    max_iter = 0
    max_num = 0
    for i in range(2, limit):
        iter_num = collatz_seq(i)
        if iter_num > max_iter:
            max_iter = iter_num
            max_num = i
        if i % (limit//20) == 0:
            print(i)
    print(max_num, max_iter)
    collatz_seq(max_num, True)
    print("******************* En buyuk Collatz sayısı ******************\n")


def aykiri_durumlar():
    print("******************* Aykırı durumlar ******************")
    try:
        print(35+45)
        val = 3/0
    except TypeError:
        print("Deger hatasi")
    except ZeroDivisionError:
        print("Sifira bolme hatasi")
    print("******************* Aykırı durumlar ******************\n")
