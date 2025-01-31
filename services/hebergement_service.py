from services.service_base import ServiceBase

class ServiceHebergement(ServiceBase):
    def __init__(self):
        super().__init__('data/hebergements.json')
