class Zwierze():
    def __init__(self, nazwa, wiek, waga):
        self.nazwa = nazwa
        self.wiek = wiek
        self.waga = waga

    def przedstaw_sie(self):
        print(
            f"Jestem zwierzeciem {self.nazwa}, mam {self.wiek} lat oraz wage {self.waga} kg.")

    def urodziny(self):
        self.wiek += 1

    def grubasek(self):
        self.waga += 1



class Slon(Zwierze):
    pass


class Papuga(Zwierze):
    pass


class Lew(Zwierze):
    pass


def main():
    Dumboo = Slon("Dumboo", 77, 6000)
    Simba = Lew("Simba", 24, 100)
    jakis_zwierz = Zwierze("Pawel", 29, 69)
    Jago = Papuga("Jago", 32, 3)


    Dumboo.przedstaw_sie()
    Simba.przedstaw_sie()
    jakis_zwierz.przedstaw_sie()

    Jago.urodziny()
    Jago.grubasek()
    Jago.przedstaw_sie()




if __name__ == "__main__":
    main()
