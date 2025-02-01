from services.service_base import ServiceBase

class ServiceClient(ServiceBase):
    def __init__(self):
        super().__init__('data/clients.json')

    def get_by_id(self, id_client):
        for client in self.donnees:
            if client["id_client"] == id_client:
                return client
        return None