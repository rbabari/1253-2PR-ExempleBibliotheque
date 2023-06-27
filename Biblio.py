class Emprunt:
    def __init__(self, numEmprunt, doc, adherent, employe, dateDuPret ):
        self.numEmprunt =numEmprunt
        self.doc = doc
        self.adherent =adherent
        self.employe =employe
        self.dateDuPret = dateDuPret

    def __str__(self):
        return "[Emprunt titre : " + str(self.doc) + " date : " + self.dateDuPret + " ]"


class Biblio:
    def __init__(self):
        self.listeDocuments = []
        self.listeAdherents = []
        self.listeEmprunts = []



    # --------------------Méthodes Document
    def ajouterDocument(self, doc):
        self.listeDocuments.append(doc)

    def listerDocuments(self):
        for x in self.listeDocuments:
            print(x) # x est de type Docuement il a __str__ comme déja définit

    def supprimerDocument(self,doc):
        self.listeDocuments.remove(doc)

    def getDocument(self, docIndex):
        return self.listeDocuments[docIndex]
    #--------------------Méthodes Adherent
    def ajouterAdhrent(self, adherent):
        self.listeAdherents.append(adherent)

    def listerAdhrents(self):
        for x in self.listeAdherents:
            print(x)  # x est de type Docuement il a __str__ comme déja définit

    def supprimerAdherent(self, adherent):
        self.listeAdherents.remove(adherent)

    def getAdherent(self, adherentIndex):
        return self.listeAdherents[adherentIndex]
   #--------------------Méthodes Emplrunts

    def ajouterEmplrunt(self, empr):
        self.listeEmprunts.append(empr)

    def listerEmplrunts(self):
        for x in self.listeEmprunts:
            print(x)  # x est de type Docuement il a __str__ comme déja définit

    def supprimerEmplrunt(self, empr):
        self.listeEmprunts.remove(empr)

    def getEmplrunt(self, emprIndex):
        return self.listeEmprunts[emprIndex]
