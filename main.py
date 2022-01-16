from Ders01 import Degiskenler as deg
from Ders01 import Dallanma as dal
from Ders02 import Donguler as don2
from Ders03 import Donguler as don3
from Ders03 import Strings
from Ders04 import Fonksiyonlar as fonk
from Ders05 import Listeler as lists
from Ders06 import Dictionaries as dicts
from Ders07 import DirectoriesFiles as df
from Ders07 import FileProcessing as fp
from Ders08 import ComplexNumber as CN
from Ders08.Pisti import Oyna
from Ders09 import Logging as lo
from Ders09 import BasicTests as bt
from Ders09 import TestCalculator as ut
from Ders09 import DocTests as dt
# from Ders10 import FlaskApp as fa

from HomeWorkSolutions import Homework1 as HW1
from HomeWorkSolutions import Homework2 as HW2
from HomeWorkSolutions import Homework3 as HW3
from HomeWorkSolutions import Homework4 as HW4


def ders01_ornekler():
    deg.print_and_input()
    deg.formatted_print()
    dal.bmi_oneri_1()
    dal.bmi_oneri_2()


def ders02_ornekler():
    don2.basit_dongu()
    don2.not_ortalama()
    don2.sayi_oyunu()


def ders03_ornekler():
    don3.sayi_tahmin_oyunu()
    don3.for_piramitler()
    don3.ic_ice_for()
    Strings.raw_strings()
    Strings.string_operators()
    Strings.indexing_slicing()
    Strings.string_methods()


def ders04_ornekler():
    fonk.fonksiyon_tanimlama()
    fonk.degis_tokus()
    fonk.euclid_alg()
    fonk.find_largest_collatz(10000)
    fonk.aykiri_durumlar()
    HW1.soru1()
    HW1.soru2()
    HW1.soru3()


def ders05_ornekler():
    HW2.soru1()
    HW2.soru2()
    HW2.soru3()
    lists.liste_yaratma()
    lists.liste_operatorleri()
    lists.liste_iterasyon()
    lists.liste_eleman_silme()
    lists.liste_metotları()
    lists.tuples()
    lists.liste_referans()


def ders06_ornekler():
    HW3.test_dice_roller()
    HW3.test_i_goal()
    HW4.test_q1()
    HW4.test_q2()
    dicts.init_dict()
    dicts.iterating_dictionaries()


def ders07_ornekler():
    df.working_with_dirs()
    df.abs_relative_paths()
    df.copy_move_delete()
    df.tree_walk()
    df.compression()
    fp.file_operations()
    fp.csv_files()
    fp.json_files()


def ders08_ornekler():
    print("******************* Working with classes and objects ******************")
    var = CN.ComplexNumber(3, 5)
    var_2 = CN.ComplexNumber(2, 7)

    print(var+var_2)
    var.new_val = 10
    print(var.new_val)

    Oyna.oyun()
    print("******************* Working with classes and objects ******************\n")


def ders09_ornekler():
    # lo.logging_example()
    # bt.basics()
    # bt.test_avg()
    # bt.test_stdev()
    ut.run_tests()
    dt.run_tests()


if __name__ == "__main__":
    # ders01_ornekler()
    # ders02_ornekler()
    # ders03_ornekler()
    # ders04_ornekler()
    # ders05_ornekler()
    # ders06_ornekler()
    # ders07_ornekler()
    # ders08_ornekler()
    ders09_ornekler()
    # ders10_ornekler()