class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def calculer_aire(self):
        return 3.14 * self.rayon ** 2

cercle1 = Cercle(7)

print("Aire du cercle :", cercle1.calculer_aire())