from services.service_base import ServiceBase

class ServiceClient(ServiceBase):
    def __init__(self):
        super().__init__('data/clients.json')
