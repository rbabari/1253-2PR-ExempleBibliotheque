# Creer un document

class Document:
    def __init__(self, titre, nbrPages, numISBN):
        self.titre = titre
        self.nbrPages = nbrPages
        self.numISBN = numISBN

    def __str__(self):
        return "[Doc: " + self.titre + "]"

    @staticmethod
    def lireClavier():
        print("----SAISIR DOUMENT ----")
        titre = input("Document.titre : ")
        nbrPages = input("Document.nbrPages : ")
        numISBN = input("Document.numISBN : ")
        return Document(titre, nbrPages, numISBN)


class Livre(Document):
    def __init__(self, doc, auteur, maisonEdition):
        super().__init__(doc.titre, doc.nbrPages, doc.numISBN)
        self.auteur = auteur
        self.maisonEdition = maisonEdition

    def __str__(self):
        return "[Livre: " + self.titre + " ecris par : " + self.auteur + "]"

class Journal(Document):
    def __init__(self, doc, dateDePublication):
        super().__init__(doc.titre, doc.nbrPages, doc.numISBN)
        self.dateDePublication = dateDePublication
    def __str__(self):
        return "[Journal: " + self.titre + " paru le : " + self.dateDePublication + "]"

