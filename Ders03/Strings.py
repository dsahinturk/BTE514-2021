def raw_strings():
    print("******************* Raw and multiline strings ******************")
    val = r"Tolga Ovatman\n"
    print(val, end="")

    double = "Tolga 'Ovatman\n"
    print(double, end="")

    single = 'Tolga "Ovatman\n'
    print(single, end="")

    triple = ''' sdfsd 
    "  'sfsd
    sdfsdf\n
    sdfsdf
    '''
    print(triple, end="")
    print()
    print("******************* Raw and multiline strings ******************\n")



def indexing_slicing():
    print("******************* Indexing and slicing strings ******************")

    strng = "Tolga Ovatman"
    print(strng[3])

    i = 0
    while i < len(strng):
        print(strng[i], end=".")
        i += 1
    print()

    print(strng[3:7])
    print(strng[:7])
    print(strng[2:-2])
    print("******************* Indexing and slicing strings ******************\n")


def string_operators():
    print("******************* String operators ******************")
    print("Tolga"+" Ovatman")
    str1 = "lg"
    str2 = "Tolga"
    print(str1 in str2)

    print('+'*5)
    print("******************* String operators ******************\n")


def string_methods():
    print("******************* String methods ******************")
    strng = "Tolga Ovatman"
    print(strng.upper())
    print('-5'.isnumeric())
    print('-5'.isdigit())
    strng = '    \tTo lga   \n  '
    print(strng.strip())
    print(strng.strip().replace(' ', ''))


    strng = "Hayriye Duygu Ozkan Ovatman"
    splitted = strng.split(' ')
    print(splitted)
    print("-".join(splitted))

    print(strng.rfind("u"))
    print("******************* String methods ******************\n")

