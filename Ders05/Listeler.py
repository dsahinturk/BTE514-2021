import math
import copy


def liste_yaratma():
    print("******************* Liste yaratma ******************")
    a_list = []
    print(a_list)
    a_list = [3, 5, 7, 9, 11]
    print(a_list)
    print(a_list[2])
    print(a_list[1:4])
    a_list = [4, 18.35, "Tolga", [3, 5, 7]]
    print(a_list[2].upper())
    print(a_list[2][-1])
    print(a_list[3][2])
    a_list = [i**2 if i%2==0 else math.sqrt(i) for i in range(10)]
    print(a_list)
    print("******************* Liste yaratma ******************\n")

def liste_operatorleri():
    print("******************* Liste operatörleri ******************")
    a_list = [1, 2, 3, 4, 5]
    b_list = [10, 9, 8, 7, 6]

    print(a_list*3)
    print([[1, 2]]*3)

    print(a_list + b_list)
    a_list.append(b_list)
    print(a_list)

    print(6 not in b_list)
    print("******************* Liste operatörleri ******************\n")


def liste_iterasyon():
    print("******************* Liste iterasyon ******************")
    a_list = [1, 2, 3, 4, 5]
    b_list = [10, 9, 8, 7, 6]

    print(a_list + b_list)
    a_list.append(b_list)

    print([i*3 for i in a_list])
    for i in a_list:
        print(i, end=" ")
    print()

    for i in range(len(a_list)):
        print(a_list[i], end=" ")
    print()
    print("******************* Liste iterasyon ******************\n")


def liste_eleman_silme():
    print("******************* Listeden eleman silme ******************")
    a_list = [1, 2, 3, 4, 5]
    a_list.remove(3)
    print(a_list)

    del a_list[2]
    print(a_list)
    print("******************* Listeden eleman silme ******************\n")


def liste_metotları():
    print("******************* Liste metotları ******************")
    a_list = [1, 2, 3, 4, 5]
    a_list[0] = 10
    a_list[1:3] = [8, 8]
    print(a_list)

    for i in range(len(a_list)):
        a_list.append(a_list[i]*2)

    print(a_list)
    print(a_list.index(20))
    a_list.insert(a_list.index(20)+1, 21)
    print(a_list)
    print(sorted(a_list))
    a_list.sort()
    print(a_list)
    for i in reversed(a_list):
        print(i, end=" ")
    print()
    a_list.reverse()
    print(a_list)

    a_list.extend(reversed(a_list))
    print(a_list)
    print("******************* Liste metotları ******************\n")


def multiple_return():
    return 3, 5

def tuples():
    print("******************* Tuples ******************")
    a_tuple = (2, 3, 4)
    print(a_tuple)
    #a_tuple[2] = 5
    a_list = list(a_tuple)
    print(a_list)
    a = 5
    b = 3

    a, b = b, a
    a, b = multiple_return()
    print(a, b)

    a_list = [4]
    a_tuple = (4,)
    print("******************* Tuples ******************\n")


def liste_parametre(a_list):
    a_list[0] = 15


def liste_referans():
    print("******************* Referans değerler ******************")
    a_list = [1, 2, 3, 4, 5]
    c_list = [1, 2, 3, 4, 5]
    b_list = a_list
    #b_list[0] = 10
    #print(a_list)
    print(a_list is b_list)

    liste_parametre(a_list)
    print(a_list)

    b_list = a_list.copy()
    print(a_list is b_list)
    b_list[0] = 1000
    print(a_list)
    print(b_list)

    a_list = [1, 2, 3, [5, 6, 7]]
    b_list = a_list.copy()
    #b_list[3] = a_list[3].copy()

    b_list[0] = 100
    b_list[3][0] = 100
    print(a_list)
    c_list = copy.deepcopy(a_list)
    c_list[0] = 500
    c_list[3][0] = 500
    print(a_list)
    print("******************* Referans değerler ******************\n")