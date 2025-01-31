class Chambre:
    def __init__(self, id_chambre, id_hebergement, type_chambre, prix, disponible=True):
        self.id_chambre = id_chambre
        self.id_hebergement = id_hebergement
        self.type_chambre = type_chambre
        self.prix = prix
        self.disponible = disponible

    def to_dict(self):
        return self.__dict__

class ChambreSimple(Chambre):
    def __init__(self, id_chambre, id_hebergement, prix, disponible=True):
        super().__init__(id_chambre, id_hebergement, "Simple", prix, disponible)

class ChambreDouble(Chambre):
    def __init__(self, id_chambre, id_hebergement, prix, disponible=True):
        super().__init__(id_chambre, id_hebergement, "Double", prix, disponible)

class Suite(Chambre):
    def __init__(self, id_chambre, id_hebergement, prix, disponible=True):
        super().__init__(id_chambre, id_hebergement, "Suite", prix, disponible)
