



# test pour document
from Document import Document, Livre, Journal
from Personne import Adherent, Personne, Employee
from Biblio import Biblio, Emprunt

d1 = Document("python pour les pro", "420", "123456789432")
print(d1)
l1 = Livre(Document("Miserable" ,"500" , "12345566"), "V Hugo", " Maison Montréal")
print(l1)
j1 = Journal(Document("La presse" ,"30" , "1234423566"), "27062023" )
print(j1)

# Pourquoi la class ? Créer un vocabulaire ? des nouveaux types de
# donnée avec des fonctionnalité/méthode/fonctions/procedures

a1 = Adherent(Personne("chettoh", "Fares", 26), 10001 )
print(a1)

emp1 = Employee(Personne("Agsous", "Nabil", 33), 90001 )
print(emp1)



#d2 = Document.lireClavier() # méthode static
#print(d2)

maBiblio = Biblio()
maBiblio.ajouterAdhrent(a1)
maBiblio.ajouterDocument(Document("Bricolage",300, 123456789 ))
emprunt1 = Emprunt(10001, d1, a1, emp1, "20230627" )
maBiblio.ajouterEmplrunt(emprunt1)

maBiblio.listerDocuments()
maBiblio.listerAdhrents()
maBiblio.listerEmplrunts()







