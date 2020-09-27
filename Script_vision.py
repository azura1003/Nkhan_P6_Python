import os # Ensemble de dictionnaires permettant d'utiliser les fonctionnalités notamment celles de  Windows.
import datetime
import psutil
import win32serviceutil
   
   
LOOKUP_SERVICE = 'Audiosrv' #On assigne à la variable le nom du service à tester
 
try:
    service = psutil.win_service_get(LOOKUP_SERVICE)  # Le script va chercher le service et s'il n'existe pas va afficher un message
except psutil.NoSuchProcess:
    print("service introuvable")
else:
    print("service trouvé.")   # Le service est trouvé cependant le if va confirmer s'il est en cours d'excution
    if service.status() == 'running':
        print("service est en cours de fonctionnement") # si le statut est égal à running alors le programme s'arrête
    else:
        print("service est arreté") # Si le programme est arrêté le script va le relancer
        win32serviceutil.StartService(LOOKUP_SERVICE)
        print("le service a été demarré")
        try:
            os.mkdir(r'C:\Ariane\Logs_script_vision') # Le script va essayer de créer un dossier
        except FileExistsError: # il va capturer l'erreur ici et afficher le message dossier existant s'il est déja présent
            print("Dossier logs déja existant")
        finally:   # Pour finir il va inscrire d'écrire le message de notre choix ainsi que la date et l'heure si le fichier existe, sinon il sera créer
            with open(r"C:\Ariane\Logs_script_vision\Visionlogs.txt", "a") as fichier:
                fichier.write(f"Le fichier vision a été relancé par notre script le :{datetime.datetime.now().ctime()}\n") #saut de ligne à la fin
