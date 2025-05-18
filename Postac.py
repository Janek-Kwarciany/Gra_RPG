from abc import ABC, abstractmethod

class Postac(ABC):
    def __init__(self, nazwa, zdrowie, sila_ataku):
        self.nazwa = nazwa
        self.zdrowie = zdrowie
        self.sila_ataku = sila_ataku
        
    @abstractmethod
    def atakuj(self, przeciwnik):
        przeciwnik.zdrowie = przeciwnik.zdrowie - self.sila_ataku
    
