# Cím;Rendező;Főszereplő;Év;Perc
# Hős;Yimou Zhang;Jet Li;2002;96
class Film:
    def __init__(self, sor: str):
        adatok = sor.strip().split(";")
        self.cim = adatok[0]
        self.rendezo = adatok[1]
        self.foSzereplo = adatok[2]
        self.ev = int(adatok[3])
        self.perc = int(adatok[4])

    def __str__(self):
        return f"Cim: {self.cim}  Rendezo: {self.rendezo} Foszereplo: {self.rendezo} ev: {self.ev} perc: {self.perc}"
