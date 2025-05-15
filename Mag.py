from Postac import Postac

import random

class Mag(Postac):
    def __init__(self, nazwa):
        zdrowie = random.randint(75, 150)
        sila_ataku = random.randint(7, 18)
        super().__init__(nazwa, zdrowie, sila_ataku)

    def atakuj(self):
        return super().atakuj()