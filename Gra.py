from Mag import Mag
from Wojownik import Wojownik

class Gra:
    def __init__(self):
        pass

    def petla_g(self):
        while 1:
            print("Podaj imie postaci:")
            nazwa = input()
            print("Wybór postaci:M-Mag,W-Wojownik")
            wybor = input()
            #obsłużyć niewłaściwy wybór
            if wybor == "M":
                postac=Mag(nazwa)
            elif wybor == "W":
                postac=Wojownik(nazwa)

