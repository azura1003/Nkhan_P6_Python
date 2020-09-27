import os
import datetime
import psutil
import win32serviceutil
   
   
LOOKUP_SERVICE = 'Audiosrv'
 
try:
    service = psutil.win_service_get(LOOKUP_SERVICE)
except psutil.NoSuchProcess:
    print("service not found")
else:
    print("service trouvé.")
    if service.status() == 'runnig':
        print("service est en cours de fonctionnement")
    else:
        print("service est arreté")
        win32serviceutil.StartService(LOOKUP_SERVICE)
        print("le service a été demarré")
        try:
            os.mkdir(r'C:\Ariane\Logs_script_vision') # on windows back-slash in path may create problems. use raw string or forward slash
        except FileExistsError: # catch specifi error consistent with the msg you print
            print("Dossier logs déja existant")
        finally:
            with open(r"C:\Ariane\Logs_script_vision\Visionlogs.txt", "a") as fichier:
                fichier.write(f"Le fichier vision a été relancé par notre script le :{datetime.datetime.now().ctime()}\n")
