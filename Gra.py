from Mag import Mag
from Wojownik import Wojownik
import random
import time

class Gra:
    def __init__(self):
        pass

    def petla_glowna(self):
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

            print(f"siła ataku={postac.sila_ataku}, zdrowie={postac.zdrowie}")
            wrog = self.losuj_wroga()
            self.walka(postac, wrog)

    def walka(self, postac, wrog):
        poczatek_walki = time.time()
        while 1:
            print('\u2694') 
            postac.atakuj(wrog)
            print(f"ilość zdrowia wroga {wrog.zdrowie}")
            if wrog.zdrowie <= 0:
                print("przegrana wroga")
                break

            print('\u2694') 
            wrog.atakuj(postac)
            print(f"ilość zdrowia postaci {postac.zdrowie}")
            if postac.zdrowie <= 0:
                print("przegrana postaci")
                break

            time.sleep(0.5)
        koniec_walki = time.time()
        print(f"czas walki {koniec_walki - poczatek_walki}")

    def losuj_wroga(self):
        postacie = {
            1 : Mag,
            2 : Wojownik
        }
        wylosowane = random.randint(1, 2)
        # print(f"wylosowany przeciwnik: {postacie[wylosowane].__name__}")

        wrog = postacie[wylosowane]("Wróg")
        print(f"wylosowany przeciwnik: {wrog.__class__.__name__}")

        return wrog
