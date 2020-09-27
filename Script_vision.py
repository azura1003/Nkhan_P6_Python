import os # Ensemble de dictionnaires permettant d'utiliser les fonctionnalites nottament windows.
import datetime
import psutil
import win32serviceutil
   
   
LOOKUP_SERVICE = 'Audiosrv' #On met dans la variable le nom du service qu'on veut tester.
 
try:
    service = psutil.win_service_get(LOOKUP_SERVICE)  # Le script va chercher le service et s'il n'existe pas va afficher un message
except psutil.NoSuchProcess:
    print("service introuvable")
else:
    print("service trouvé.")   # Le service est trouvé cependant le if va confirmer s'il est en cours d'excution
    if service.status() == 'running':
        print("service est en cours de fonctionnement") # si le statut est egale à running alors le programme s'arrete
    else:
        print("service est arreté") #Si le programme est arreté le script va le relancer
        win32serviceutil.StartService(LOOKUP_SERVICE)
        print("le service a été demarré")
        try:
            os.mkdir(r'C:\Ariane\Logs_script_vision') # Le script va essayer de créer un dossier
        except FileExistsError: # il va capturer l'erreur ici et afficher le message dossier existant s'il est déja présent
            print("Dossier logs déja existant")
        finally:   # Pour finir il va inscrire ecrire le message de notre choix ainsi que la date et l'heure si le fichier existe pas il va le créer
            with open(r"C:\Ariane\Logs_script_vision\Visionlogs.txt", "a") as fichier:
                fichier.write(f"Le fichier vision a été relancé par notre script le :{datetime.datetime.now().ctime()}\n") #saut de ligne à la fin
