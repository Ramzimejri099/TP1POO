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

    def ajouter_reservation(self, reservation):
        chambre = self.service_chambre.get_by_id(reservation.id_chambre)
        if chambre and chambre["disponible"]:
            chambre["disponible"] = False
            self.service_chambre.sauvegarder_donnees()
            self.service_reservation.ajouter(reservation)
        else:
            print("Erreur: Chambre non disponible")

    def supprimer_reservation(self, id_reservation):
        reservation = self.service_reservation.get_by_id(id_reservation)
        if reservation:
            chambre = self.service_chambre.get_by_id(reservation["id_chambre"])
            if chambre:
                chambre["disponible"] = True
                self.service_chambre.sauvegarder_donnees()
            self.service_reservation.supprimer(id_reservation)
        else:
            print("Erreur: Réservation non trouvée")

    def afficher_reservations(self):
        return self.service_reservation.afficher()