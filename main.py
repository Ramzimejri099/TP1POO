import json
from datetime import datetime

from models.client import Client
from models.hebergement import Hotel, Motel, Couette
from models.chambre import ChambreSimple, ChambreDouble, Suite
from models.reservation import Reservation
from services.gestion_service import GestionService

gestion=GestionService()
while True:
    print("\n--- Menu Gestion Service ---")
    print("1. Ajouter des données")
    print("2. Afficher les Données")
    print("3. Supprimer des données")
    print("4. Quitter")
    choix = input("Entrez votre choix: ")

    if choix == "1":
        print("\n--- Suppression ---")
        print("1. Ajouter un Client")
        print("2. Ajouter un Hébergement")
        print("3. Ajouter une Chambre")
        print("4. Ajouter une Réservation")
        choix_ajout = input("Choissiez une option: ")

        if choix_ajout == "1":
            id_client = int(input("Entrez l'ID du client: "))
            client = Client(id_client, input("Nom: "), input("Email: "), input("Téléphone: "))
            client_existant = next((cl for cl in gestion.service_client.donnees if cl["id_client"] == id_client), None)
            if client_existant :
                print("Erreur: Un cluent aavec cet ID existe déja")
            else:
                gestion.service_client.ajouter(client)

        elif choix_ajout == "2":
            id_hebergement = int(input("Entrez l'ID de l'hébergement: "))
            type_hebergement = input("Type d'hébergement (Hotel/Motel/Couette): ")
            hebergement = {"Hotel": Hotel, "Motel": Motel, "Couette": Couette}[type_hebergement](id_hebergement,input("Nom: "),input("Adresse: "))
            hebergement_existant = next((he for he in gestion.service_hebergement.donnees if he["id_hebergement"] == id_hebergement), None)
            if hebergement_existant :
                print("Erreur : Un héberegement avec cet ID existe déja")
            else:
                gestion.service_hebergement.ajouter(hebergement)

        elif choix_ajout == "3":
            id_chambre = int(input("Entrez l'ID de la chambre: "))
            id_hebergement = int(input("Entrez l'ID de l'hébergement associé: "))
            type_chambre = input("Type de chambre (Simple/Double/Suite): ")
            chambre = {"Simple": ChambreSimple, "Double": ChambreDouble, "Suite": Suite}[type_chambre](id_chambre,id_hebergement,float(input("Prix: ")),True)
            hebergement = next((he for he in gestion.service_hebergement.donnees if he["id_hebergement"] == id_hebergement), None)
            chambre_existant = next((ch for ch in gestion.service_chambre.donnees if ch["id_chambre"] == id_chambre), None)
            if chambre_existant:
                print("Erreur: Une chambre avec cet ID")
            elif not hebergement :
                print("Erreur: L'hebergement spécfié n'existe pas.")
            else:
                gestion.service_chambre.ajouter(chambre)
                gestion.ajouter_chambre_a_hebergement(chambre)

        elif choix_ajout == "4":
            id_reservation = int(input("Entrez l'ID de la réservation: "))
            id_client = int(input("ID Client: "))
            id_chambre = int(input("ID Chambre: "))
            client = next((cl for cl in gestion.service_client.donnees if cl["id_client"] == id_client), None)
            chambre = next((ch for ch in gestion.service_chambre.donnees if ch["id_chambre"] == id_chambre), None)
            if not client:
                print("Erreur: Le client spécifié n'existe pas.")
            elif not chambre:
                print("Erreur: La chambre spécifiée n'existe pas.")
            elif not chambre["disponible"]:
                print("Erreur: La chambre sélectionnée n'est pas disponible.")
            else:
                date_debut = input("Date début (YYYY-MM-DD): ")
                date_fin = input("Date fin (YYYY-MM-DD): ")
                reservation = Reservation(id_reservation, id_client, id_chambre, date_debut, date_fin)
                gestion.service_reservation.ajouter(reservation)
                gestion.mettre_a_jour_disponibilite_chambre(id_chambre, False)

        else:
            print("Choix invalide.")

    elif choix == "2":
        print("\n--- Suppression ---")
        print("1. Afficher les clients")
        print("2. Afficher les hébergements")
        print("3. Afficher les chambres")
        print("4. Afficher les réservation")
        choix_affichage = input("Choissiez une option: ")

        if choix_affichage =="1":
            gestion.service_client.afficher()

        elif choix_affichage =="2":
            gestion.service_hebergement.afficher()

        elif choix_affichage == "3":
                gestion.service_chambre.afficher()

        elif choix_affichage == "4":
                    gestion.service_reservation.afficher()
        else:
            print("Choix invalide.")

    elif choix == "3":
        print("\n--- Suppression ---")
        print("1. Supprimer un Client")
        print("2. Supprimer un Hébergement")
        print("3. Supprimer une Chambre")
        print("4. Supprimer une Réservation")
        choix_suppression = input("Choisissez une option: ")

        if choix_suppression == "1":
            id_client = int(input("Entrez l'ID de client: "))
            client = next((cl for cl in gestion.service_client.donnees if cl["id_client"] == id_client), None)
            if not client:
                print("Erreur: Le client spécifie n'existe pas")
            else:
                gestion.service_client.supprimer(id_client)

        elif choix_suppression == "2":
            id_hebergement=int(input("Entrez l'ID d'hébergement "))
            hebergement = next((he for he in gestion.service_hebergement.donnees if he["id_hebergement"] == id_hebergement), None)
            if not hebergement :
                print("Erreur: L'hébergement spécifie n'existe pas")
            else:
                gestion.service_hebergement.supprimer(id_hebergement)

        elif choix_suppression == "3":
            id_chambre=int(input("Entrer l'ID de chambre"))
            chambre = next((ch for ch in gestion.service_chambre.donnees if ch["id_chambre"] == id_chambre),None)
            if not chambre:
                print("Erreur: La chambre spécifié n'existe pas")
            else:
                gestion.service_chambre.supprimer(id_chambre)

        elif choix_suppression == "4":

            id_reservation = int(input("Entrez l'ID de reservation: "))
            reservation = next((res for res  in gestion.service_reservation.donnees if res["id_reservation"] == id_reservation), None)
#            if not reservation:
#                print("Erreur: La réservation spécifie n'existe pas")
#            else:
            gestion.service_reservation.supprimer(id_reservation)
            gestion.mettre_a_jour_disponibilite_chambre(reservation["id_chambre"], True)
        else:
            print("Choix invalide.")

    elif choix == "4":
        print("Merci d'avoir utiliser le systéme")
        break

    else:
        print("Choix invalide. Veuillez réessayer.")


