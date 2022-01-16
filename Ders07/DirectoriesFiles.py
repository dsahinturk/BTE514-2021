import os
import shutil
import zipfile


def working_with_dirs():
    print("******************* Directory operations ******************")
    # Aşağıdaki kodlar için ilgili klasörleri kendi sisteminize göre düzeltmeniz gerekir
    print(os.getcwd())
    os.chdir(r"C:\Users\ovatm\Downloads")
    print(os.getcwd())
    os.makedirs(r"Tolga3\Tolga4")
    os.chdir(r"C:\Users\ovatm\Downloads\TolgaBTE")
    print(os.getcwd())
    print("******************* Directory operations ******************\n")


def abs_relative_paths():
    print("******************* Absolute and relative paths ******************")
    # Aşağıdaki kodlar için ilgili klasörleri kendi sisteminize göre düzeltmeniz gerekir
    print(os.getcwd())
    print(os.path.abspath("."))
    print(os.path.abspath(r"..\..\repos"))
    print(os.path.relpath(r"C:\Users\ovatm\Source\repos"))
    print(os.path.isabs(r"..\ovatm\Source\repos"))
    print(os.path.sep)
    str_path = os.path.split(r"C:\Users\ovatm\Source\repos")
    print(os.path.split(str_path[0]))
    print(r"C:\Users\ovatm\Source\repos".split(os.path.sep))
    fpath = r"C:\Users\ovatm\Source\PycharmProjects\BTE514-2021\main.py"
    print(os.path.basename(fpath))
    print(os.path.dirname(fpath))
    fpath = r"C:\Users\ovatm\Source\PycharmProjects\BTE514-2021\main2.py"
    print(os.path.basename(fpath))
    print(os.path.isdir(fpath))
    print(os.path.exists(fpath))
    print("******************* Absolute and relative paths ******************\n")


def copy_move_delete():
    print("******************* Copy, move and delete operations ******************")
    # Aşağıdaki kodlar için ilgili klasörleri kendi sisteminize göre düzeltmeniz gerekir
    os.remove(r"C:\Users\ovatm\Source\PycharmProjects\BTE514-2021\deneme\deneme.txt")
    os.rmdir(r"C:\Users\ovatm\Source\PycharmProjects\BTE514-2021\Deneme")
    shutil.rmtree(r"C:\Users\ovatm\Source\PycharmProjects\BTE514-2021\Deneme")
    shutil.copy(r"src\dene.txt", r"dst\dene2.txt")
    shutil.move(r"dst\dene2.txt", r"dst\dene_new.txt")
    shutil.copytree("src", "dst\src_new")
    print("******************* Copy, move and delete operations ******************\n")


def tree_walk():
    print("******************* Walk directory tree ******************")
    # Aşağıdaki kodlar için ilgili klasörleri kendi sisteminize göre düzeltmeniz gerekir
    all_file_names = []
    for elm in os.walk(r"C:\Users\ovatm\Source\PycharmProjects\BTE514-2021"):
        if ".git" not in elm[0]:
            all_file_names += elm[2]
            # all_file_names = all_file_names.union(set(elm[2]))

    count = 0
    for i in set(all_file_names):
        print(i, end=" ")
        count += 1
        if count % 5 == 0:
            print()

    print("******************* Walk directory tree ******************\n")


def compression():
    print("******************* Compression ******************")
    # Aşağıdaki kodlar için ilgili klasörleri kendi sisteminize göre düzeltmeniz gerekir
    my_zip = zipfile.ZipFile("my_dirs.zip", "w")
    my_zip.write("dst")
    my_zip.write("src")
    my_zip.close()
    my_zip = zipfile.ZipFile("my_dirs.zip", "r")
    print(my_zip.namelist())
    print(my_zip.filelist)
    print("******************* Compression ******************\n")
