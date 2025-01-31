class Reservation:
    def __init__(self, id_reservation, id_client, id_chambre, date_debut, date_fin):
        self.id_reservation = id_reservation
        self.id_client = id_client
        self.id_chambre = id_chambre
        self.date_debut = date_debut
        self.date_fin = date_fin

    def to_dict(self):
        return self.__dict__
