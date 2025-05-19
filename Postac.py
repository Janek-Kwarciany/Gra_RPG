from abc import ABC, abstractmethod
import random

class Postac(ABC):
    def __init__(self, nazwa, zdrowie, sila_ataku):
        self.nazwa = nazwa
        self.zdrowie = zdrowie
        self.sila_ataku = sila_ataku
        
    @abstractmethod
    def atakuj(self, przeciwnik):
        przeciwnik.zdrowie = przeciwnik.zdrowie - self.sila_ataku
    
    def wyposazenie(self):
        zbroja_1 = self.zdrowie + 30
        zbroja_2 = self.zdrowie + 50
        losuj_zbroje = {
            1 : zbroja_1,
            2 : zbroja_2
        }
        wylosowana_zbroja= random.randint(1, 2)
        zbroja = losuj_zbroje[wylosowana_zbroja]
        print(f"wylosowano zbroję: {wylosowana_zbroja}")
        self.zdrowie = zbroja
        