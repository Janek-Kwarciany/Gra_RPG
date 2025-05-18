from Postac import Postac

import random

class Wojownik(Postac):
    def __init__(self, nazwa):
        zdrowie = random.randint(100, 200)
        sila_ataku = random.randint(10, 20)
        super().__init__(nazwa, zdrowie, sila_ataku)

    def atakuj(self, przeciwnik):
        super().atakuj(przeciwnik)
