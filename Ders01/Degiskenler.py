def print_and_input():
    print("******************* input output ******************")
    print("Hello", "World", "!!!", sep="--", end=">>>>")
    print()
    age = input("Your age: ")
    a = 30
    n = "Tolga"
    s = "Ovatman"
    mystr = "Hello Mr.{surname}, your age is {age}"
    print(mystr.format(age=a, surname=s))
    print("******************* input output ******************\n")


def formatted_print():
    print("******************* formatted output ******************")
    isim = input("Adınızı yazınız: ")
    dogum = input("Dogum yiliniz: ")
    print("Merhaba {0}, {1} yaşındasın.".format(isim, 2021 - int(dogum)))
    print("******************* formatted output ******************\n")
