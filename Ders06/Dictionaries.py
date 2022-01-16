def init_dict():
    print("******************* Initialize and access dictionary ******************")
    a_dict = {}
    a_dict['Tolga'] = "Ovatman"
    a_dict[('Tolga', 'Ayse')] = "Ovatman"
    a_dict['Tolga'] = {'Ayse': 'Ovatman'}
    a_dict['Duygu'] = "Ozkan"
    a_dict['Cenk'] = "Cicen"

    print(a_dict)
    print(a_dict['Duygu'])
    print(a_dict['Tolga']['Ayse'])

    b_dict = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    b_dict[(1, 2, 3)] = "Tolga"
    b_dict[(1, 2, 3)] = "Murat"
    print(b_dict)
    print("******************* Initialize and access dictionary ******************\n")

def iterating_dictionaries():
    print("******************* Iterate dictionary ******************")
    a_dict = {"Tolga": 123, "Murat": 131, "Sahin": 634}

    print(a_dict)

    for a in a_dict:
        print(a_dict[a])

    for key in a_dict.keys():
        print(a_dict[key])

    for val in a_dict.values():
        print(val)

    for item in a_dict.items():
        print(item)

    print("******************* Iterate dictionary ******************\n")
