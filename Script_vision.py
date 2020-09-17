import psutil
import win32serviceutil
import os
import datetime


def getService(Audiosrv):
    service = None
    try:
        service = psutil.win_service_get(Audiosrv)
        service = service.as_dict()
    except Exception as ex:
        print (str(ex))

    return service

service = getService('Audiosrv')

#print(service)

if service:
        print ("service trouvé")
else:
        print ("service not found")

if service and service['status'] == 'running':

        print ("service est en cours de fonctionnement")
else:

         print ("service est arreté")
         service = "Audiosrv"
         win32serviceutil.StartService(service)
         print("le service a été demarré")
         try:
             os.mkdir('C:\Ariane\Logs_script_vision')
         except:
             print("Dossier logs déja existant")
         finally:
             fichier = open("C:\Ariane\Logs_script_vision\Visionlogs.txt","a")
             fichier.write("\nLe fichier vision a été relancé par notre script le :")
             fichier.write(datetime.datetime.now().ctime())
             fichier.close()
