from services.client_service import ServiceClient
from services.hebergement_service import ServiceHebergement
from services.chambre_service import ServiceChambre
from services.reservation_service import ServiceReservation

class GestionService:
    def __init__(self):
        self.service_client = ServiceClient()
        self.service_hebergement = ServiceHebergement()
        self.service_chambre = ServiceChambre()
        self.service_reservation = ServiceReservation()

    def ajouter_chambre_a_hebergement(self, chambre):
        hebergement = self.service_hebergement.get_by_id(chambre.id_hebergement)
        if hebergement:
            hebergement.setdefault("chambres", []).append(chambre.to_dict())
            self.service_hebergement.sauvegarder_donnees()
        else:
            print("Erreur: Hébergement introuvable")

    def mettre_a_jour_disponibilite_chambre(self, id_chambre, disponible):
        chambres = self.service_chambre.donnees
        for chambre in chambres:
            if chambre["id_chambre"] == id_chambre:
                chambre["disponible"] = disponible
                self.service_chambre.sauvegarder_donnees()
                break