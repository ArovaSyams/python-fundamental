
class Tabungan:
    def __init__(self, uang=0, koin=0):
        self.uang = uang
        self.koin = koin

    def __str__(self):
        return f"{self.uang} uang, {self.koin} koin"
    
    def __add__(self, other):
        uang = self.uang + other.uang
        koin = self.koin + other.koin
        return Tabungan(uang, koin)

wifqo = Tabungan(100, 50)
print(wifqo)

arova = Tabungan(25, 300)
print(arova)

total = wifqo + arova
print(total)
        