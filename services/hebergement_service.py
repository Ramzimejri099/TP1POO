from services.service_base import ServiceBase

class ServiceHebergement(ServiceBase):
    def __init__(self):
        super().__init__('data/hebergements.json')

    def get_by_id(self, id_hebergement):
        for hebergement in self.donnees:
            if hebergement["id_hebergement"] == id_hebergement:
                return hebergement
        return None