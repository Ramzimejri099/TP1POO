import json
from datetime import datetime
from services.gestion_service import GestionService

from models.client import Client
from models.hebergement import Hotel, Motel, Couette
from models.chambre import ChambreSimple, ChambreDouble, Suite
from models.reservation import Reservation

gestion=GestionService()
while True:
    print("\n--- Menu Gestion Service ---")
    print("1. Gestion des Clients")
    print("2. Gestion des Hébergements")
    print("3. Gestion des Chambres")
    print("4. Gestion des Réservations")
    print("5. Quitter")
    choix = input("Entrez votre choix: ")

    if choix == "1":
        id_client = int(input("Entrez l'ID du client: "))
        client = Client(id_client, input("Nom: "), input("Email: "), input("Téléphone: "))
        gestion.service_client.ajouter(client)
        print("Client ajouté avec succès!")

    elif choix == "2":
        id_hebergement = int(input("Entrez l'ID de l'hébergement: "))
        type_hebergement = input("Type d'hébergement (Hotel/Motel/Couette): ")
        hebergement = {"Hotel": Hotel, "Motel": Motel, "Couette": Couette}[type_hebergement](id_hebergement, input("Nom: "), input("Adresse: "))
        gestion.service_hebergement.ajouter(hebergement)
        print("Hébergement ajouté avec succès!")

    elif choix == "3":
        id_chambre = int(input("Entrez l'ID de la chambre: "))
        type_chambre = input("Type de chambre (Simple/Double/Suite): ")
        id_hebergement = input("Entrez l'ID de l'hebergement")
        chambre = {"Simple": ChambreSimple, "Double": ChambreDouble, "Suite": Suite}[type_chambre](id_chambre, id_hebergement, float(input("Prix: ")), True)
        gestion.service_chambre.ajouter(chambre)
        print("Chambre ajoutée avec succès!")

    elif choix == "4":
        id_reservation = int(input("Entrez l'ID de la réservation: "))
        reservation = Reservation(id_reservation, int(input("ID Client: ")), int(input("ID Chambre: ")), input("Date début (YYYY-MM-DD): "), input("Date fin (YYYY-MM-DD): "))
        gestion.ajouter_reservation(reservation)
        print("Réservation effectuée avec succès!")

    elif choix == "5":
        print("Merci d'avoir utilisé le système!")
        break

    else:
        print("Choix invalide. Veuillez réessayer.")

