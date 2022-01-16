'''
    :param deger Cevirilmesi istenen sicaklik degeri
    :param birim Gonderilen sicaklik degerinin birimi
    :return donusmus deger
'''


def sicaklik_donusumu(deger, birim="C"):
    # try:
    if birim == "C":
        return deger * 1.8 + 32
    elif birim == "F":
        return (deger - 32) / 1.8
    else:
        raise Exception("Donusum birimi hatali")

    # except:
    #    print("Kodda bir hata olustu")
    #    return 0


def increasing_decreasing(num1, num2, num3):
    if num1 > num2 > num3:
        print("Decreasing")
    elif num1 < num2 < num3:
        print("Increasing")
    else:
        print("Neither")


def print_increasing(num1, num2, num3):
    print(min(num1, num2, num3), end=" ")
    print(num1 + num2 + num3 - min(num1, num2, num3) - max(num1, num2, num3), end=" ")
    print(max(num1, num2, num3))


def test_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def test_leap_2(year):
    print("******************* Soru 2 cozum 2 ******************")

    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def test_leap_3(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False


def soru1():
    print("******************* Soru 1 cozum ******************")
    print(sicaklik_donusumu(32, "F"))
    print("******************* Soru 1 cozum  ******************\n")


def soru2():
    print("******************* Soru 2 cozum ******************")
    increasing_decreasing(5, 7, 7)
    print_increasing(5, 9, 1)
    print("******************* Soru 2 cozum ******************\n")


def soru3():
    print("******************* Soru 3 cozum ******************")
    print(test_leap(1900))
    print(test_leap_2(2000))
    print(test_leap_3(1904))
    print("******************* Soru 3 cozum ******************\n")
