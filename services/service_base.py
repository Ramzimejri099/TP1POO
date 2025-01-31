import json

class ServiceBase:
    def __init__(self, fichier):
        self.fichier = fichier
        self.donnees = self.charger_donnees()

    def charger_donnees(self):
        try:
            with open(self.fichier, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def sauvegarder_donnees(self):
        with open(self.fichier, 'w') as f:
            json.dump(self.donnees, f, indent=4)

    def ajouter(self, obj):
        self.donnees.append(obj.to_dict())
        self.sauvegarder_donnees()

    def supprimer(self, id_obj):
        self.donnees = [obj for obj in self.donnees if obj.get('id_client', obj.get('id_hebergement', obj.get('id_chambre', obj.get('id_reservation')))) != id_obj]
        self.sauvegarder_donnees()

    def afficher(self):
        return self.donnees
