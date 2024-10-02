class Personne:
    def __init__(self, nom):
        self.nom = nom

    def se_presenter(self):
        print(f"Bonjour, je m'appelle {self.nom}")

personne1 = Personne("Ruben")

personne1.se_presenter()