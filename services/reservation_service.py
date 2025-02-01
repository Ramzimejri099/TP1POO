from services.service_base import ServiceBase

class ServiceReservation(ServiceBase):
    def __init__(self):
        super().__init__('data/reservations.json')

    def get_by_id(self, id_reservation):
        for reservation in self.donnees:
            if reservation["id_reservation"] == id_reservation:
                return reservation
        return None