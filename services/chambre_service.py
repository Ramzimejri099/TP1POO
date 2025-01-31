from services.service_base import ServiceBase

class ServiceChambre(ServiceBase):
    def __init__(self):
        super().__init__('data/chambres.json')

    def get_by_id(self, id_chambre):
        for chambre in self.donnees:
            if chambre["id_chambre"] == id_chambre:
                return chambre
        return None
