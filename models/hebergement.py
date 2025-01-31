class Hebergement:
    def __init__(self, id_hebergement, nom, adresse, type_hebergement):
        self.id_hebergement = id_hebergement
        self.nom = nom
        self.adresse = adresse
        self.type_hebergement = type_hebergement
        self.chambres = []

    def ajouter_chambre(self, chambre):
        self.chambres.append(chambre)

    def to_dict(self):
        return {
            "id_hebergement": self.id_hebergement,
            "nom": self.nom,
            "adresse": self.adresse,
            "type_hebergement": self.type_hebergement,
            "chambres": [chambre.to_dict() for chambre in self.chambres]
        }

class Hotel(Hebergement):
    def __init__(self, id_hebergement, nom, adresse):
        super().__init__(id_hebergement, nom, adresse, "Hotel")

class Motel(Hebergement):
    def __init__(self, id_hebergement, nom, adresse):
        super().__init__(id_hebergement, nom, adresse, "Motel")

class Couette(Hebergement):
    def __init__(self, id_hebergement, nom, adresse):
        super().__init__(id_hebergement, nom, adresse, "Couette")
