def soru1():
    print("******************* Soru 1 cozum ******************")
    print("Lutfen sayılar girin, durmak için -1 girin")
    val = int(input())
    min_so_far = val
    max_so_far = val
    while val != -1:
        if val < min_so_far:
            min_so_far = val
        if val > max_so_far:
            max_so_far = val
        val = int(input())

    print("En buyuk sayı", max_so_far)
    print("En küçük sayı", min_so_far)
    print("******************* Soru 1 cozum  ******************\n")


def soru2():
    print("******************* Soru 2 cozum ******************")
    x = 45763
    while x > 0:
        print(x % 10, end="")
        x = x // 10
    print()
    print("******************* Soru 2 cozum ******************\n")


def soru3():
    print("******************* Soru 3 cozum ******************")
    base = input("Taban metni giriniz: ")
    sub = input("Aranacak metni giriniz: ")
    num = int(input("Tekrar sayısını giriniz: "))

    if len(base)<=0 or len(sub)<=0 or num<0:
        print("Hatalı girdi")
        exit(1)

    final_ind = 0
    for i in range(num-1):
        ind = base.find(sub)
        final_ind += ind+len(sub)
        base = base[ind+len(sub):]

    if base.find(sub) >= 0:
        final_ind += base.find(sub)
    else:
        final_ind = -1

    print(final_ind)

    print("******************* Soru 3 cozum ******************\n")
