class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def calculer_aire(self):
        return self.longueur * self.largeur

    def calculer_perimetre(self):
        return 2 * (self.longueur + self.largeur)

rectangle1 = Rectangle(10, 5)

print("Aire du rectangle :", rectangle1.calculer_aire())
print("Périmètre du rectangle :", rectangle1.calculer_perimetre())