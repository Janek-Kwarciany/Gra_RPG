from Postac import Postac

import random

class Mag(Postac):
    def __init__(self, nazwa):
        zdrowie = random.randint(75, 150)
        sila_ataku = random.randint(7, 18)
        super().__init__(nazwa, zdrowie, sila_ataku)

    def atakuj(self, przeciwnik):
        losuj_podwojny_atak = random.randint(1, 10)
        pierwotna_sila_ataku = self.sila_ataku

        if losuj_podwojny_atak == 1:
            self.sila_ataku = self.sila_ataku * 2

        super().atakuj(przeciwnik)
        self.sila_ataku = pierwotna_sila_ataku
