from abc import ABC, abstractmethod


class Zwierze(ABC):
    def __init__(self, nazwa, wiek, waga):
        self.nazwa = nazwa
        self.wiek = wiek
        self.waga = waga

    @abstractmethod # tutaj wymuszamy implementację tej metody w klasach pochodnych
    def nazwa_gatunku(self):
        pass
    
    def przedstaw_sie(self):
        print(
            f"Jestem {self.nazwa_gatunku()}, Mam na imię {self.nazwa}, mam {self.wiek} lat oraz wage {self.waga} kg.")

    def urodziny(self):
        self.wiek += 1

    def grubasek(self):
        self.waga += 1


class Slon(Zwierze):
    def nazwa_gatunku(self):
        return "Slon"
    pass


class Papuga(Zwierze):
    def nazwa_gatunku(self):
        return "Papuga"
    pass



    def __init__(self, nazwa, wiek, waga, kolor):
        super().__init__(nazwa, wiek, waga)
        self.kolor = kolor

    def przedstaw_sie(self):
        super().przedstaw_sie()
        print(f"Jako papuga mój kolor to {self.kolor}")


class Lew(Zwierze):
    def nazwa_gatunku(self):
        return "Lew"
    pass


def nowy_rok(zoo):
    for zwierze in zoo:
        zwierze.urodziny()


def przedstaw_zwierzeta(zoo):
    for zwierze in zoo:
        zwierze.przedstaw_sie()


def main():
    Dumboo = Slon("Dumboo", 77, 6000)
    Simba = Lew("Simba", 24, 100)
    # jakis_zwierz = Zwierze("Pawel", 29, 69)
    Jago = Papuga("Jago", 32, 3, "czerwony")

    Dumboo.przedstaw_sie()
    Simba.przedstaw_sie()
    # jakis_zwierz.przedstaw_sie()

    Jago.urodziny()
    Jago.grubasek()
    Jago.przedstaw_sie()

    # zoo = [Dumboo, Simba, Jago, jakis_zwierz]
    # nowy_rok(zoo)
    # przedstaw_zwierzeta(zoo)


if __name__ == "__main__":
    main()
