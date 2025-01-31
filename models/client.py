class Client:
    def __init__(self,id_client,nom,courriel,telephone):
        self.id_client = id_client
        self.nom = nom
        self.courriel = courriel
        self.telephone = telephone

    def to_dict(self):
        return self.__dict__