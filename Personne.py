class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
    def __str__(self):
        return "[Personne: " + self.nom + " " + self.prenom + "]"

class Adherent(Personne):
    def __init__(self, personne, numAdherent):
        super().__init__(personne.nom, personne.prenom, personne.age)
        self.numAdherent = numAdherent

    def __str__(self):
        return "[Adherent: " + self.nom + " num :  " + str(self.numAdherent) + "]"

class Employee(Personne):
    def __init__(self, personne, numEmployee):
        super().__init__(personne.nom, personne.prenom, personne.age)
        self.numEmployee = numEmployee

    def __str__(self):
        return "[Employee: " + self.nom + " num :  " + str(self.numEmployee) + "]"
