"""Module pour modifier les données des objets. Tant que les 'magic methods' ne sont pas utilisés (sauf pour __init__), ils sont bien codés et seraient prêt à être implémentés dans une expansion du programme si nécessaire."""

class Jeu:
    
    def __init__(self, nom): # Défini les propriétés des objets
        self._strnom = nom
        self._lstdeveloppeur = []
        self._lstgenre = []
        self._intannee = None
        self._lstlangue = []
    
    def __str__(self): # Imprime un message
        return f"Le nom du jeu vidéo est: '{self._strnom}'."
    
    def __getitem__(self, position):
        return {
            "developpeur": self._lstdeveloppeur[position] if position < len(self._lstdeveloppeur) else None,
            "genre": self._lstgenre[position] if position < len(self._lstgenre) else None,
            "langue": self._lstlangue[position] if position < len(self._lstlangue) else None,
        }
    
    def __len__(self):
        return (len(self._lstdeveloppeur), len(self._lstgenre), len(self._lstlangue))
    
    def ajout_objet_dev(self, strObjet): # Fonction pour ajouter et supprimer un élément des listes
        self._lstdeveloppeur.append(strObjet)
        
    def supp_objet_dev(self, strObjet):
        self._lstdeveloppeur.remove(strObjet)

    def ajout_objet_genre(self, strObjet):
        self._lstgenre.append(strObjet)
        
    def supp_objet_genre(self, strObjet):
        self._lstgenre.remove(strObjet)
    
    def ajout_objet_langue(self, strObjet):
        self._lstlangue.append(strObjet)

    def supp_objet_langue(self, strObjet):
        self._lstlangue.remove(strObjet)
    
    @property # Décorations pour chaque propriétés
    def strnom(self):
        return self._strnom
        
    @strnom.setter
    def strnom(self, strvaleur):
        self._strnom = strvaleur
        
    @property 
    def lstdeveloppeur(self):
        return self._lstdeveloppeur
        
    @lstdeveloppeur.setter
    def lstdeveloppeur(self, lstvaleur):
        self._lstdeveloppeur = lstvaleur
        
    @property 
    def lstgenre(self):
        return self._lstgenre
        
    @lstgenre.setter
    def lstgenre(self, lstvaleur):
        self._lstgenre = lstvaleur
        
    @property
    def intannee(self):
        return self._intannee
        
    @intannee.setter
    def intannee(self, intvaleur):
        self._intannee = intvaleur
        
    @property
    def lstlangue(self):
        return self._lstlangue
        
    @lstlangue.setter
    def lstlangue(self, lstvaleur):
        self._lstlangue = lstvaleur