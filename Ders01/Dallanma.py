def bmi_oneri_1():
    print("******************* BMI Öneri 1 ******************")
    kilo = int(input("Kilonuzu giriniz:"))
    boy = float(input("Boyunuzu giriniz:"))
    bmi = kilo / boy ** 2

    # a = "T" if 5>3 else "H"

    if 18 < bmi < 24:
        print("Kilonuz iyi")
    elif bmi < 18:
        print("Kilonuz iyi degil")
        print("Biraz kilo alabilirsiniz")
    elif bmi > 24:
        print("Kilonuz iyi degil")
        print("Biraz kilo verebilirsiniz")
    print("******************* BMI Öneri 1 ******************\n")


def bmi_oneri_2():
    print("******************* BMI Öneri 2 ******************")
    kilo = int(input("Kilonuzu giriniz:"))
    boy = float(input("Boyunuzu giriniz:"))
    bmi = kilo / boy ** 2

    if 18 < bmi < 24:
        print("Kilonuz iyi")
    else:
        print("Kilonuz iyi degil")
        if bmi <= 18:
            print("Biraz kilo alabilirsiniz")
        elif bmi >= 24:
            print("Biraz kilo verebilirsiniz")

    print("Bye!!")
    print("******************* BMI Öneri 2 ******************\n")
